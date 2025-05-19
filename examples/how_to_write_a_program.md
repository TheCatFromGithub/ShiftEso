# How to write a program

All whitespace is ignored.
ShiftEso works on an MxN grid. You can declare the size at the start:
`2x2` (2 wide, 2 high)
If ShiftEso doesn't find it, it will assume a size of 16x16. There are two basic registers: `$` and `%`. Both start at 0, and are 64 bit signed integers. (Python has unlimited size ints, but this project uses NumPy arrays.) You can increment `$` with `+`. You can decrement it with `-`. You can set `%` to `$` with `#`, and set `$` to `%` with `@`. You can set `$` to `$` mod 256 with `!`. Print `$` with `.` (`$` mod 256), and read one byte of input in with `;` and store it in `$` (if no input is left, it reads in 0). `[` jumps to the corresponding `]` if `$` is zero, and `]` jumps to the corresponding `[` if `$` is nonzero.

`>`, `<`, `^`, and `v` all take two parameters.
`>x,y` shifts row x one step  to the right and inserts y at the end. The value that "fell out" is stored in `$`. x and y can be an int, `$`, or `%`. Note that the value to insert is computed AFTER the shift has been done, so you can `>0,$` to rotate row 0 to the right.
`<x,y` is like `>x,y` but it shifts row x to the left instead of the right.
`^x,y` is like `>x,y` but shifts **column** x up.
`vx,y` is like `^x,y` but shifts column x down.

Again, all whitespace is ignored.
Also, all the indicies are mod the max, so if you can put in an index of -1 to get the last row/col, -2 to get the penultimate row/col.
