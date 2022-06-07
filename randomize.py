from random import *
print()
print('Добро пожаловать в числовую угадайку!')
while True:
    n = randrange(1, 101)
    try_counter = 0


    def digit_guess(num):  # угадываем число
        counter = 1
        while num != n:
            if num > n:
                num = int(input('Ваше число больше загаданного, попробуйте еще разок: '))
            elif num < n:
                num = int(input('Ваше число меньше загаданного, попробуйте еще разок: '))
            counter += 1
        global try_counter
        try_counter = counter


    def is_valid(num):  # проверяем вадидность введенного числа
        if 0 < num < 101:
            return True
        else:
            return False


    s = int(input('Пожалуйста, введите число от 1 до 100: '))

    while not is_valid(s):
        s = int(input('А может быть все-таки введем целое число от 1 до 100? : '))

    digit_guess(s)
    print()
    print('Вы угадали число с', try_counter , 'попыток, поздравляем!')
    print('Спасибо, что играли в числовую угадайку. Введите новое число и сыграйте снова!')