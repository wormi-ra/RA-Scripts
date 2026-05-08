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

struct XContainer {
    u32 meta[7];
    char key[] @ meta[5];
    u32 *data: u32;
} [[inline]];

struct XomData {
    u32;
    u32 ptr;
    XContainer container@ ptr;
} [[inline]];

struct Pointer {
    u32 value [[hidden]];
    if (value != 0x0) {
        XomData data@ value [[hidden]];
        char key[] @ data.container.meta[5];
    }
} [[inline]];

u32 size @ 0x01CE36F0;
Pointer hashmap[size] @0x01ce3700;