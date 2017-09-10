def fibonacci(n):
    i = 0
    a, b = 0, 1
    while i < n:            
        print(a)
        a, b = b, a + b
        i += 1

fibonacci(10)