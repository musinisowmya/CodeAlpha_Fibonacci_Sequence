def fibonacci_iterative(n):
    """
    Generate Fibonacci sequence using an iterative approach.
    
    Args:
        n (int): Number of Fibonacci numbers to generate
    
    Returns:
        list: Fibonacci sequence
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)
    
    return fib_sequence

def fibonacci_recursive(n):
    """
    Generate Fibonacci sequence using a recursive approach.
    
    Args:
        n (int): Number of Fibonacci numbers to generate
    
    Returns:
        list: Fibonacci sequence
    """
    def fib(k):
        if k <= 1:
            return k
        return fib(k-1) + fib(k-2)
    
    return [fib(i) for i in range(n)]

def fibonacci_generator(n):
    """
    Generate Fibonacci sequence using a generator function.
    
    Args:
        n (int): Number of Fibonacci numbers to generate
    
    Returns:
        generator: Fibonacci sequence generator
    """
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

# Demonstration
print("Iterative Method:")
print(fibonacci_iterative(10))

print("\nRecursive Method:")
print(fibonacci_recursive(10))

print("\nGenerator Method:")
print(list(fibonacci_generator(10)))

# Performance and space complexity demonstration
import timeit

def performance_comparison():
    iterations = 30
    
    iterative_time = timeit.timeit(
        lambda: fibonacci_iterative(iterations), 
        number=1000
    )
    
    recursive_time = timeit.timeit(
        lambda: fibonacci_recursive(iterations), 
        number=1000
    )
    
    generator_time = timeit.timeit(
        lambda: list(fibonacci_generator(iterations)), 
        number=1000
    )
    
    print(f"\nPerformance Comparison (lower is better):")
    print(f"Iterative Method: {iterative_time:.5f} seconds")
    print(f"Recursive Method: {recursive_time:.5f} seconds")
    print(f"Generator Method: {generator_time:.5f} seconds")

performance_comparison()