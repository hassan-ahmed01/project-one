#TASK FOUR 
def fibonacci_series(n):
    x = [0, 1]
    while len(x) < n:
        x.append(x[-1] + x[-2])
    return x

n = 8
result_fibonacci = fibonacci_series(n)
 
print("fibonacci final series", result_fibonacci)