
num = float(input("Введите число: "))

def sumNums(num):
    sum = 0
    for i in str(num):
        if i != ".":
            sum += int(i)
    return sum

print(f"Сумма цифр = {sumNums(num)}")