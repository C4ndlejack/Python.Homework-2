num = int(input("Введите число n: "))
sum = 0
list = []
for i in range(1, num + 1):
    result = round((1 + 1 / i) ** i)
    list.append(result)
    sum += result

print(list)
print(sum)