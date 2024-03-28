import time

def factorial(n):
  # A function that returns the factorial of n
  if n == 0 or n == 1:
    return 1
  else:
    return n * factorial(n-1)

# Start the timer
start = time.time()

# Call the factorial function with n = 10
result = factorial(10)

# Stop the timer
end = time.time()

# Print the result and the elapsed time
print(f"The factorial of 10 is {result}")
print(f"The function took {end - start} seconds to execute")
