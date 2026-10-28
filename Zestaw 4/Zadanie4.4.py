def fibonacci(n):
    x, y, z  = 0, 1, 0
    for i in range(0 , n):
        z = x + y
        x = y
        y = z
    return x 
print(fibonacci(4))