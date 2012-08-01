interpreter
===========
Interpreter of a very simple language, working on a set of four variables (A, B, C and D) and supporting the following set of operations:

    V = A
    V += A
    V -= A
    V *= C

Where V is any variable, C is a constant and A is either variable or a constant.
It also supports loops, for example

    A = 1
    loop 100
    A *= 2
    end
    end

(here first `end` ends the loop and the second `end` ends the program) will compute 2 to the power of 100.
The interesting thing about this interpreter is that it performs loops in O(log N) operations, where N is the number of iterations. For example the following code will compute the sum of first 10^18 numbers:

    loop 1000000000
    loop 1000000000
    A += 1
    B += A
    end
    end
    end

It will immediately print

    [1000000000000000000L, 500000000000000000500000000000000000L, 0L, 0L]

Where second number represents the value of B after the program execution.

