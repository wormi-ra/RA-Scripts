// Enter your pattern code here and click on the Play button
// below to execute your code. The results will then be visible
// in the Pattern Data view.
// 
// More information can be found in the documentation.
// 
// 
// Simple example:
// 
// import std.io;
// 
// struct Pattern {
//     u32 int;
//     float floating_point;
// };
// 
// Pattern my_pattern @ 0x00;
// std::print("0x{:08X}", my_pattern.int);

struct ArenaImpl {
    u32 unk0;
    u32 address;
    u32 size;
    u32 allocated;
    u32 unk10 [[hidden]];
    u32 unk14 [[hidden]];
    u32 unk18 [[hidden]];
    u32 unk1c [[hidden]];
    u32 unk20 [[hidden]];
    u32 unk24 [[hidden]];
    u32 elementSize;
    u32 unk2c [[hidden]];
    u32 unk30 [[hidden]];
    u32 name_ptr [[hidden]];
    u32 unk38 [[hidden]];
    u32 unk3c [[hidden]];
    char name[] @ name_ptr;
};

struct Arena {
    u32 impl_ptr [[hidden]];
    u32 index;
    ArenaImpl impl @ impl_ptr [[inline]];
};

struct Pointer {
    u32 ptr [[hidden]];
    Arena data @ ptr [[inline]];
};

//u32 memoryManager @ 0x6b84d8;
Pointer arenaList[20] @ 0x6b84d8;