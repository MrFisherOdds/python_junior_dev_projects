from random import *

n = randrange(1, 101)

def digit_guess(num):  # угадываем число
    while num != n:
        if num > n:
            num = int(input('Ваше число больше загаданного, попробуйте еще разок: '))
        elif num < n:
            num = int(input('Ваше число меньше загаданного, попробуйте еще разок: '))


def is_valid(num):  # проверяем вадидность введенного числа
    if 0 < num < 101:
        return True
    else:
        return False

print()
print('Добро пожаловать в числовую угадайку!')
print()

s = int(input('Пожалуйста, введите число от 1 до 100: '))

while not is_valid(s):
    s = int(input('А может быть все-таки введем целое число от 1 до 100?'))

digit_guess(s)
print()
print('Вы угадали, поздравляем!')
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')







