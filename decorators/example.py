import functools


def debug_output(function):	
	def wrapper(*args, **kwargs):
		print(function.__name__, args, kwargs)

		return function(*args, **kwargs)

	return wrapper


@debug_output
def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n - 1)

# factorial = debug_output(factorial)


print(factorial(5))

a = [1, 2, 3, 4, 5]
kwargs = {'file': open('output.txt', 'w')}
print(*a, **kwargs)

@functools.lru_cache()
def fib(n):
	if n == 1 or n == 2:
		return 1
	else:
		return fib(n - 1) + fib(n - 2)

print(fib(100))
