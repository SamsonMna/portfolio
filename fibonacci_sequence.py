# Fibonacci sequence
# 1 1 2 3 5 8.....

def fibonacci(n):
    seq = [0, 1]
    while len(seq) < n:
        next_num = seq[-1] + seq[-2]
        seq.append(next_num)
    return seq
    
    
    
# Say you wanna have the function output ten numbers
# just call the function and give the desired output as an argument
fibonacci(10) # Add you have the numbers
