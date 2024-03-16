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
        for idx in range(length):
                breakpoint()
                fib_seq.append(0)
                fib_seq.append(1)
                sum = fib_seq[-2] + fib_seq[-1]
                fib_seq.append(sum)
        print(fib_seq)
        

# below in place of line 5?
        #idx = len(fib_seq)
        
# def print_fibonacci(length):
#     fib_seq = []
#     if length == 0:
#         print(fib_seq)
#     elif length == 1:
#         fib_seq.append(0)
#         print(fib_seq)
#     elif length == 2:
#         fib_seq.append(0)
#         fib_seq.append(1)
#         print(fib_seq)
#     else:
#         for idx in range(length):
#             if len(fib_seq) == 0:
#                 fib_seq.append(0)
#                 print(fib_seq)
#                 return
#             elif len(fib_seq) == 1:
#                 fib_seq.append(1)
#                 print(fib_seq)
#                 return
#             elif len(fib_seq) >= 2:
#                 print(fib_seq)
#                 sum = fib_seq[-2] + fib_seq[-1]
#                 fib_seq.append(sum)
#                 print(fib_seq)
#                 print(fib_seq[idx])
