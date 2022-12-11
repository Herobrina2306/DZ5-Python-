# 2 Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все
# конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"


from random import randint
 
CANDIES = 80
MAX_STEP = 28
 
human = True
cur_candies = CANDIES
 
 
def get_ai_step(l):
    if cur_candies < 28:
        return cur_candies
    else:
        f = (MAX_STEP+1) - l 
        return f
 
 
def get_human_step():
    while True:
        cnt = input('Введите количество конфет: ')
        if cnt.isdigit() and 1 <= int(cnt) <= min(MAX_STEP, cur_candies):
            return int(cnt)
        print('Введено некорректное значение')
 
 
while cur_candies:
    if human:
        cat = get_human_step()
        cur_candies -= cat
        print(f'Пользователь взял {cat} конфет. Осталось {cur_candies}.')
    else:
        cnt = get_ai_step(cat)
        cur_candies -= cnt
        print(f'Бот взял {cnt} конфет. Осталось {cur_candies}.')
    human = not human
 
if human:
    print('Победил БОТ')
else:
    print('Победил человек')