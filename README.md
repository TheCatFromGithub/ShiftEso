# ShiftEso

**ShiftEso** is a new esoteric programming language (esolang) created by TheCatFromGithub in 2025. The following is a guide on how to use it.

# Requirements

- Python 3.10+
- NumPy

# Running a program

Simply edit your main.py file, set `stored_in` to whatever Unicode sequence you want the interpreter to read in, and at the bottom, change `interpret("+[.+!]")` to whatever ShiftEso program you want. 

# Examples

You can find ShiftEso examples in the examples/ folder.

# Writing a program

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

# License

The main project is licensed under the MIT License.  
However, all contents of the `examples/` folder are released into the public domain under the [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/) dedication.
