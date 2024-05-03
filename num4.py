# Задание 4 - декоратор

def decor(func):
    def wrapper(*args, **kwargs):
        print(f"'{func.__name__}'. \n {args}; {kwargs}")
        result = func(*args, **kwargs)
        return result



    return wrapper


@decor




def fib(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

n = int(input("Кол-во чисел: "))

fibo = fib(n)

print(f"Первые {n} чисел Фибоначчи:")
for num in fibo:
    print(num, end=" ")
