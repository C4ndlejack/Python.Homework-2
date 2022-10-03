n = int(input("Введите число n: "))

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

list = []
for i in range(1, n + 1):
    list.append(factorial(i))

print(f"Произведения чисел от 1 до {n}:  {list}")
