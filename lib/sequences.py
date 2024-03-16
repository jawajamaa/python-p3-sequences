#!/usr/bin/env python3
def print_fibonacci(length):
    fib_seq = []
    if length == 0:
        print(fib_seq)
    elif length == 1:
        fib_seq.append(0)
        print(fib_seq)
    elif length == 2:
        fib_seq.append(0)
        fib_seq.append(1)
        print(fib_seq)
    else:
        fib_seq.append(0)
        fib_seq.append(1)
        sum = fib_seq[-2] + fib_seq[-1]
        fib_seq.append(sum)
        if length == 3: 
             print(fib_seq)
             return
        elif length > 3:
            for idx in range(length-3):
                sum = fib_seq[-2] + fib_seq[-1]
                fib_seq.append(sum)
        print(fib_seq)
        
