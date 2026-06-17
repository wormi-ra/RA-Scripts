# Working with Lua 5 Memory in RetroAchievements

### A guide by [Wormi](https://retroachievements.org/user/Wormi)

# Table of Content
- [Context](#context)
  - [Why Lua 5?](#why-lua-5)
  - [Scope](#scope)
- [Working with Lua Memory](#working-with-lua-memory)
  - [1. Extracting Lua scripts](#1-extracting-lua-scripts)
  - [2. Identifying the Lua version](#2-identifying-the-lua-version)
  - [3. Digging in Lua memory](#3-digging-in-lua-memory)
  - [4. Finding the Lua State and Global Table addresses](#4-finding-the-lua-state-and-global-table-addresses)
  - [5. Lua Nodes and Table structure](#5-lua-nodes-and-table-structure)
  - [6. Calculating offsets in the Global Table](#6-calculating-offsets-in-the-global-table)
  - [7. Using Lua memory in achievement logic](#7-using-lua-memory-in-achievement-logic)
  - [8. Automation](#8-automation)
- [Closing Words](#closing-words)
- [References](#references)

## Context

During my journey of developping achievements for [Worms 3D on the PS2](https://retroachievements.org/game/21184), I faced Lua memory and learned a lot about Lua's inner mechanisms and wanted to share my experience for other developpers wanting to take on future sets with games using Lua.

This guide only covers Lua 5 and will probably make some assumptions since every game and system is different and that Worms 3D is the only game using Lua I worked on so far, but I hope this guide will help and motivate other developpers to work with Lua games.

### Why Lua 5?

Lua 5 released in 2003 and became a very popular scripting language for video games especially for consoles such as the PS2 and Wii. If your game uses Lua and has been released after 2003, there are very high chances it is Lua 5.

Between Lua 4 and Lua 5, the entire `Table` data structure has been reimplemented, so a good portion of the guide won't apply here. Though the Lua 4 `Table` data structure is probably easier to work with.

More info about the Lua 5 implementation is available here:
[The Implementation of Lua 5.0](https://www.lua.org/doc/jucs05.pdf)

### Scope

This guide will cover making logic with global variables lying in the Lua scripts. This assumes the scripts are relatively simple and that your achievements only rely on one or two variables at most within the script (Usually a flag or a counter that cannot be found outside of the Lua memory).

Working with local variables within a Lua function is probably possible by following the function's `Closure` data structure and finding it's associated `Table` but this guide won't cover it.

Due to the complexity of Lua memory allocation, it is only advised to use it as a last ressort. Most games uses Lua as a scripting language to communicate with the game engine (usually written in C or C++) and exposes memory that lives in the game engine to the Lua scripts. This memory is usually easier to work with directly, but in some cases, some important variables responsible for triggering events are only exposed in Lua memory.

## Working with Lua Memory

### 1. Extracting Lua scripts

Extracting the Lua scripts from the game ROM is very valuable for learning how the game works and figuring out which variables can be used in your achievement logic.
Each game and system is different so I won't go into details on how to extract the files but they're usually stored in plain `.lua` files inside the game ROM or `.lub` compiled Lua files that can still be decompiled.

If you cannot figure out how to extract the files, you can alternatively look into the game memory for big chunks of text, the game will usually load the script in memory at some point. Try searching for ASCII strings of Lua keywords such as `function`, `do`, `end`, `global`...

### 2. Identifying the Lua version

Identifying the exact version will let you know which version of the [Lua source code](https://www.lua.org/source/) to look for. Some functions or data structure will vary depending on the Lua version. When searching for a specific memory structure, you might want to look at how the structure is defined in the Lua source code.

One easy way to identify the version is to search for the ASCII string `Lua ` (with a space)
This will usually result in the Lua copyright string which, for Worms 3D, looks like this:
```
Lua 5.0
Copyright (C) 1994-2003 Tecgraf, PUC-Rio
R. Ierusalimschy, L. H. de Figueiredo & W. Celes
```

The exact version's source code can be downloaded here if not available in the Lua docs: https://www.lua.org/ftp/

### 3. Digging in Lua memory

Lua numbers are represented as floating points, even when interpreted as integers.
You will often encounter values such as:
- `0x3f800000` (1.0)
- `0x40000000` (2.0)
- `0x40400000` (3.0)
- Etc...

The exact representation may vary depending on the system architecture but you can convert floats using this tool: [Floating Point to Hex Converter](https://gregstoll.com/~gregstoll/floattohex/)

> [!NOTE]
> There is a Lua compilation option that allows numbers to be stored as integers but it is very unlikely to be used in a video game.

Start by looking for a simple global variable in a specific script that is predictable, easy to manipulate and in a reproducible environment.

> [!TIP]
> A global variable is a variable that is prefixed by the keyword `global` or no keyword at all. As opposed to the `local` keyword which declares a local variable to the function's scope.

In this example, I will use the Worms 3D mission [Rum Deal](https://www.youtube.com/watch?v=Lcnz0XCDaTo).

```Lua
-- rum.lua from Worms 3D

function Initialise()
    cdestroy = 0
    -- [Omitted code for simplicity]...
end

function Crate_Destroyed()
    cdestroy = cdestroy + 1

    -- [Omitted code for simplicity]...

    if cdestroy == 3 then
        if Switch == 0 then
            -- [Mission failure logic]
            Switch = 1
        end
    end 
end
```

Here, `cdestroy` is the amount of crates destroyed in the Rum Deal mission.
The mission fails once you have destroyed 3 crates.
Let's say I want to find the address to this `cdestroy` variable.
It is trivial to find it using constant compare with the `float32` type, comparing against `0.0` on mission start, `1.0` after destroying one crate, `2.0` after destroying a second crate, and so on...

> [!WARNING]
> The variable might get reallocated at any time when performing ingame actions as the Lua script executes so keep your actions very simple if possible, try other variables or other scripts if search attempts keep failing.

Repeat the operation on different save states by doing exactly the same actions in the same order every time, this is important so that the Lua functions are always executed in the same order. You should now have multiple save states with either exactly the same address or slightly varying addresses. This should also give you an idea of where lies the Lua memory range.

### 4. Finding the Lua State and Global Table addresses

The `Lua State` structure is the absolute root for our Lua memory. Depending on how dynamic is your game's memory, it could or could not be allocated at the same address every time. For Worms 3D, the `Lua State` and Global `Table` structure were allocated at deterministic addresses.

> [!NOTE]
> It is not necessary, but having knowledge about C memory alignment and padding and knowing how to read C structs really helps figuring out how the data is laid out in memory.

Lua State implementation in Lua 5.0

```C
// lstate.h from Lua source code

/*
** Union of all collectable objects
*/
union GCObject {
  GCheader gch;
  union TString ts;
  union Udata u;
  union Closure cl;
  struct Table h;
  struct Proto p;
  struct UpVal uv;
  struct lua_State th;  /* thread */
};

struct lua_State {
  CommonHeader;
  StkId top;  /* first free slot in the stack */
  StkId base;  /* base of current function */
  global_State *l_G;
  CallInfo *ci;  /* call info for current function */
  StkId stack_last;  /* last free slot in the stack */
  StkId stack;  /* stack base */
  int stacksize;
  CallInfo *end_ci;  /* points after end of ci array*/
  CallInfo *base_ci;  /* array of CallInfo's */
  unsigned short size_ci;  /* size of array `base_ci' */
  unsigned short nCcalls;  /* number of nested C calls */
  lu_byte hookmask;
  lu_byte allowhook;
  lu_byte hookinit;
  int basehookcount;
  int hookcount;
  lua_Hook hook;
  TObject _gt;  /* table of globals */
  GCObject *openupval;  /* list of open upvalues in this stack */
  GCObject *gclist;
  struct lua_longjmp *errorJmp;  /* current error recover point */
  ptrdiff_t errfunc;  /* current error handling function (stack index) */
};
```

```C
// lobject.h from Lua source code

typedef struct Table {
  CommonHeader;
  lu_byte flags;  /* 1<<p means tagmethod(p) is not present */ 
  lu_byte lsizenode;  /* log2 of size of `node' array */
  struct Table *metatable;
  TObject *array;  /* array part */
  Node *node;
  Node *firstfree;  /* this position is free; all positions after it are full */
  GCObject *gclist;
  int sizearray;  /* size of `array' array */
} Table;
```

What we're looking for is the `_gt` (table of globals) property of `Lua State` then the `node` pointer of the `Table` struct, as well as the `lsizenode` property (which should be 8-bit). `_gt->node` is where are stored all the global variables, including the `cdestroy` variable we're looking for.

Using [PointerFinder2](https://github.com/CySlaytor/PointerFinder2) with the save states we created earlier, we should find at least one converging pointer chain to this table of global.
It may or may not be the base address or our pointer chain depending on how dynamic is your game so take time to analyse what's in surrounding memory in each step of the chain.

Alternatively, if you have access to a debugger and your game ROM has debugging symbols enabled (rare but it was the case for the Europe ROM of Worms 3D), you can use breakpoints on most of the `lua_*` functions, for example the `luaH_set` function.
Otherwise use a breakpoint on the address of the variable you found previously and perform an action ingame to make it change.
Most Lua functions pass a pointer to the Lua State as their first parameter. For the PS2 that means that the Lua State will usually be found in the `a0` register.

With the help of both PF2, the debugger, and analysing memory myself, I was able to figure out the whole pointer chain:
```
[32-bit Pointer] Lua State
+0x44: [32-bit Pointer] Table of globals (state->_gt)
++0x7: [8-bit] Vector Size (state->_gt->lsizenode)
++0x10: [32-bit Pointer] Global Node Vector (state->gt->node)
+++0xa48: [32-bit Float] cdestroy variable
```

Again, exact offsets may vary depending on your Lua version and system architecture but should be similar.

> [!NOTE]
> PF2 might find one or more additional `+0x10` or `+0xc` pointers at the end of the chain. This is normal and will be explained in the next step.

### 5. Lua Nodes and Table structure

We now have a working pointer chain to our variable, but only under certain conditions and can break unexpectedly depending on the player actions.
Now let's see how the `Table` data structure works.

In Lua 5, this is implemented as a [Chained Scatter Table](https://book.huihoo.com/data-structures-and-algorithms-with-object-oriented-design-patterns-in-c++/page230.html).
It essentially is a contiguous memory vector that uses string hashes as index just like an associative array except that each "slot" is actually a node in a linked list.
This linked list is used to handle hash collisions by creating a node in the next empty slot and by appending it to the linked list of it's current node. That means you are not guaranteed to find the variable you are looking for in the first node directly, but you are guaranteed to find it if you follow the linked list.
This is a very efficient hybrid data structure but unfortunately a pain to work with in the RA toolkit.

Here's the node definition in Lua 5.0:

```C
// lua.h from Lua source code

/*
** basic types
*/
#define LUA_TNONE	(-1)

#define LUA_TNIL	0
#define LUA_TBOOLEAN	1
#define LUA_TLIGHTUSERDATA	2
#define LUA_TNUMBER	3
#define LUA_TSTRING	4
#define LUA_TTABLE	5
#define LUA_TFUNCTION	6
#define LUA_TUSERDATA	7
#define LUA_TTHREAD	8
```
```C
// lobject.h from Lua source code

/*
** Union of all Lua values
*/
typedef union {
  GCObject *gc;
  void *p;
  lua_Number n;
  int b;
} Value;

typedef struct lua_TObject {
  int tt; /* object type */
  Value value;
} TObject;

typedef struct Node {
  TObject i_key;
  TObject i_val;
  struct Node *next;  /* for chaining */
} Node;
```

This is a lot of information at once, but let's keep things simple.
A `Node` is composed of a `key`, a `value` and a pointer to the next `Node`
In the Global Table, all keys are of type TSTRING (4), and the value we are looking for is of type TNUMBER (3)

On the PS2, a node is 20 bytes long (again, implementation can vary with system architecture) and follow this structure:
```
Lua Node
+0x0: [32-bit] Key type (Always 4 for strings)
+0x4: [32-bit Pointer] Pointer to key string
++0x8: [32-bit] String hash
++0xc: [32-bit] String length
++0x10: [ASCII] Key string
+0x8: [32-bit] Value type (Always 3 for numbers)
+0xc: [32-bit Float] Value
+0x10: [32-bit Pointer] Pointer to next node
```

### 6. Calculating offsets in the Global Table

The offset for a given node is calculated using the following formula:

> (StringHash % (1 << LSizeNode)) * sizeof(Node)

`StringHash` being the precomputed Lua string hash of said variable, `LSizeNode` being the Log2 size of the vector and `sizeof(Node)` is 20.
This means that the offset varies depending on the vector size (which is always a power of two and can only grow as the script runs).

Let's grab our variable's key hash by following the key pointer from our node
From there we should be able to see the hash (32-bit) followed by the string length (also 32-bit) then the string itself `cdestroy`.
It's hash value is `0x87652183`.

During my playtesting, I have been watching how the `LSizeNode` value from the Global Table evolves.
It starts at `0x7` during the mission's intro cutscene and changes to `0x8` as soon as the cutscene ends.

`LSizeNode` is the Log2 size of the node vector, the vector size is always a multiple of two, that means for a `LSizeNode` of `0x8` the vector is 256 nodes long.

Here's the representation of the `LSizeNode` values:
```
0x0 = 1
0x1 = 2
0x2 = 4
0x3 = 8
0x4 = 16
0x5 = 32
0x6 = 64
0x7 = 128
0x8 = 256
0x9 = 512
0xa = 1024
0xb = 2048
0xc = 4096 (Theoretical max before memory runs out in Worms 3D)
and so on...
```

Every time the `LSizeNode` value changes, the node vector is reallocated, and nodes are reinserted into the new vector, Keep that in mind when searching for a specific variable.

If we take our `cdestroy` example, the offset for a `LSizeNode` value of `0x8` is: 

> (0x87652183 % 256) * 20 = 0xa3c

Add to that `0xc` to get the value of the node and we end up with `0xa48` which match exactly the offset that we found earlier with PF2.

### 7. Using Lua memory in achievement logic

Unfortunately, the RA toolkit doesn't support the bitshift `<<` operator as of this date so we cannot compute the offset directly. Instead we have to resort to alt groups or duplicate conditions for each different `LSizeNode` value.

With our `cdestroy` example:
```
LSizeNode | Node Offset
0x1 = 0x14
0x2 = 0x3c
0x3 = 0x3c
0x4 = 0x3c
0x5 = 0x3c
0x6 = 0x3c
0x7 = 0x3c
0x8 = 0xa3c
0x9 = 0x1e3c
0xa = 0x1e3c
0xb = 0x1e3c
0xc = 0x1e3c
```

We would need to create 3 different alt groups for offsets `0x3c`, `0xa3c` and `0x1e3c`. We can omit the first `LSizeNode` since it is unrealistic to have a vector of size 2.
In practice, we could only make alt groups for offsets `0x3c` and `0xa3c` and save some alt groups since the only `LSizeNode` values encountered during my playtest were `0x7` and `0x8`.

When playtesting, always play thorougly and monitor how the `LSizeNode` value changes, try playing the level in unexpected ways and note every value you encounter.

When using a Lua variable in achievement logic, always check for the string hash of the current node to avoid reading garbage memory.

Example pseudo-logic for making an achievement that require the player to complete the mission without destroying any crate would like this:

```
// LSizeNode 0x2-0x7
AddAddress  Mem 0xGlobalTable       +   Value 0x3c
AddAddress  Mem 0x4 (Key pointer)
AndNext     Mem 0x8 (String Hash)   =   Value 0x87652183
AddAddress  Mem 0xGlobalTable       +   Value 0x3c
ResetIf     Mem 0xc (Value)         !=  Value 0.0

// LSizeNode 0x8
AddAddress  Mem 0xGlobalTable       +   Value 0xa3c
AddAddress  Mem 0x4 (Key pointer)
AndNext     Mem 0x8 (String Hash)   =   Value 0x87652183
AddAddress  Mem 0xGlobalTable       +   Value 0xa3c
ResetIf     Mem 0xc (Value)         !=  Value 0.0

// LSizeNode 0x9-0x1c
AddAddress  Mem 0xGlobalTable       +   Value 0x1e3c
AddAddress  Mem 0x4 (Key pointer)
AndNext     Mem 0x8 (String Hash)   =   Value 0x87652183
AddAddress  Mem 0xGlobalTable       +   Value 0x1e3c
ResetIf     Mem 0xc (Value)         !=  Value 0.0
```

Now don't forget that the variable we're looking for can be nested in the linked list.
Fortunately, due to the nature of this data structure, nodes should rarely exceed a depth of 1 or 2, especially with large vector sizes. In my example, the node never gets allocated deeper in the linked list, but if that happened we would need to create additional conditions for each depth and repeat the process for each `LSizeNode` offsets.

```
// LSizeNode 0x2-0x7 (Depth 0)
AddAddress  Mem 0xGlobalTable       +   Value 0x3c
AddAddress  Mem 0x4 (Key pointer)
AndNext     Mem 0x8 (String Hash)   =   Value 0x87652183
AddAddress  Mem 0xGlobalTable       +   Value 0x3c
ResetIf     Mem 0xc (Value)         !=  Value 0.0

// LSizeNode 0x2-0x7 (Depth 1)
AddAddress  Mem 0xGlobalTable       +   Value 0x3c
AddAddress  Mem 0x10 (Next Node)
AddAddress  Mem 0x4 (Key pointer)
AndNext     Mem 0x8 (String Hash)   =   Value 0x87652183
AddAddress  Mem 0xGlobalTable       +   Value 0x3c
AddAddress  Mem 0x10 (Next Node)
ResetIf     Mem 0xc (Value)         !=  Value 0.0

// LSizeNode 0x2-0x7 (Depth 2)
AddAddress  Mem 0xGlobalTable       +   Value 0x3c
AddAddress  Mem 0x10 (Next Node)
AddAddress  Mem 0x10 (Next Node)
AddAddress  Mem 0x4 (Key pointer)
AndNext     Mem 0x8 (String Hash)   =   Value 0x87652183
AddAddress  Mem 0xGlobalTable       +   Value 0x3c
AddAddress  Mem 0x10 (Next Node)
AddAddress  Mem 0x10 (Next Node)
ResetIf     Mem 0xc (Value)         !=  Value 0.0
```

Due to the exponential nature of this process, things can go out of hand very quickly, that's why it is important to playtest thoroughly that way we can "hardcode" all the possible values and exclude unnecessary conditions.

Here's the real implementation of this achievement in Worms 3D if you're curious: [Grog from the Seas](https://authorblues.github.io/retroachievements/AutoCR/#!/game/21184/achievement/615550)

### 8. Automation

Now that we figured out how to make the logic, let's automate it to make the development process less painful.
I use [PyCheevos](https://github.com/CarlosNatanael/PyCheevos) to generate achievement logic, but the process should be the same in RATools or cruncheevos.

I started looking at the implementation of the lua hash function in `lstring.c` and reimplemented it in python to automatically compute the hash of a given string.

```python
class Lua:
    @staticmethod
    def string_hash(s: str)-> int:
        l = len(s)
        h = l
        step = (l >> 5) + 1
        i = l
        while i >= step:
            h = (h ^ ((h << 5) + (h >> 2) + ord(s[i-1]))) & 0xffffffff
            i -= step
        return h

    @staticmethod
    def get_index(key: str, lsize: int):
        return Lua.string_hash(key) % (1 << lsize)
```

Using this function, we can figure out the hash of any variable in the Lua script just by passing it's name to the `string_hash` function.

I then made a `Lua.Node` class to handle the code generation for a single node.
Then made a `get_node` function that retrieves the correct node address depending on the `LSizeNode` and `Depth` parameter:

```python
class Lua:
    NODESIZE = 20

    class Node:
        key: str
        hashstr: int
        address: MemoryExpression

        def __init__(self, key: str, address: MemoryExpression) -> None:
            self.key = key
            self.hashstr = Lua.string_hash(key)
            self.address = address

        def get_hash(self):
            return self.address >> dword(0x4) >> dword(0x8)

        def get_value(self):
            return self.address >> float32(0xc)

    @staticmethod
    def get_node(ctx: Context, key: str, lsize: int, depth: int):
        offset = Lua.get_index(key, lsize) * Lua.NODESIZE
        address = {
            "EU": Memory.EU_LUA_GLOBAL_TABLE_NODE_VECTOR,
            "US": Memory.US_LUA_GLOBAL_TABLE_NODE_VECTOR,
        }[ctx.region]
        address = MemoryExpression(Condition(address, "+", value(offset)), start_flag=Flag.ADD_ADDRESS)
        while depth > 0:
            address >>= dword(0x10)
            depth -= 1
        return Lua.Node(key, address)
```

The code isn't too pretty but it does exactly what you expect.
We can now use it in our achievement logic to generate code like this:

```python
for lsize in [7, 8]:
    for depth in [0, 1]:
        node = Lua.get_node(ctx, "cdestroy", lsize, depth)
        conditions.append(
            reset_if(
                (node.get_hash() == node.hashstr) &
                (node.get_value() != 0.0)
            )
        )
```

This code will generate all possible conditions for `LSizeNode` `0x7` and `0x8` with `Depth` 0 and 1 for the `cdestroy` variable.

With this toolkit, we can now generate logic without even having to calculate the node offset or search for ingame memory. Just input the correct variable name, tweak the `lsize` and `depth` parameters if necessary and voila!

## Closing Words

As you can imagine, this method cannot be used to create very complex logic without hitting some kind of limitations since using multiple Lua variables in a single achievements would multiply alt conditions exponentially.
It only works well for checking against very specific values such as event flags or counters that are not exposed in regular memory.

If you want to look at more real life examples of this implementations you can take a look at my Worms 3D code notes at address `0x17f31d0`,
as well as the python implementation of my logic in the references below.

Thank you very much for staying until the end, I hope this guide will be useful for future Lua set developpers. Do not hesitate to [contact me on the RA website](https://retroachievements.org/user/Wormi) if you need help or on the RA discord.

If you wish to improve this guide, you can contribute on github by submitting a PR or just contacting me.

## References
- [The Implementation of Lua 5.0](https://www.lua.org/doc/jucs05.pdf)
- [Lua source code](https://www.lua.org/source/)
- [Worms 3D (PS2) code notes](https://retroachievements.org/codenotes.php?g=21184)
- [Example achievement implementation](https://authorblues.github.io/retroachievements/AutoCR/#!/game/21184/achievement/615550)
- [Example achievement python source code](https://github.com/wormi-ra/RA-Scripts/blob/c2c6c86a68cb9bb73b61270c916e9ec55acb3bb7/Worms%203D%20(PS2)/set.py#L654)
- [Lua helper methods in python](https://github.com/wormi-ra/RA-Scripts/blob/c2c6c86a68cb9bb73b61270c916e9ec55acb3bb7/Worms%203D%20(PS2)/logic.py#L667)
