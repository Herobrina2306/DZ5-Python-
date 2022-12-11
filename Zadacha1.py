# 1 Напишите программу, удаляющую из файла все слова, содержащие "абв".

with open ('text.txt', 'r', encoding = 'utf-8') as f:
    lst = list(map(str, f.readline().split()))

print(lst)


substring = 'абв'
output_txt = filter(lambda x: x.lower().find(substring) == -1, lst)
print(*output_txt)

