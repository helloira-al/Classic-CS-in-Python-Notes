#the code below implements memoization explicitly to calculate the nth Fibonacci value

fibonacci_cache = {}

def fibonacci(n):
    # check if n is aleady stored in the cached values
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    # otherwise calculate the nth term

    # check if n is an integer
    if type(n) != int:
        raise TypeError("n must be a positive integer")
    # check if n is a positive integer
    if n < 1:
        raise ValueError("n must be a positive integer")

    if (n == 1):
        value = 1
    elif (n == 2):
        value = 1
    elif (n > 2):
        value = fibonacci(n - 1) + fibonacci(n - 2)

    # store the value in cache and return it
    fibonacci_cache[n] = value
    return value


# call the function
print(fibonacci(100))


