from random import *


def password_generator(pass_len, need_digits, need_uppers, need_lowers, need_symbols, need_exception):
    global digits
    global lowercase_letters
    global uppercase_letters
    global punctuation
    global exception
    spisok_vseh_elmentov = []
    user_password = []
    count_of_requirements = 0

    if need_digits == 'ДА':  # собираем требования и дополняем общий список
        spisok_vseh_elmentov.extend(digits)
        count_of_requirements += 1
    if need_uppers == 'ДА':
        spisok_vseh_elmentov.extend(uppercase_letters)
        count_of_requirements += 1
    if need_lowers == 'ДА':
        spisok_vseh_elmentov.extend(lowercase_letters)
        count_of_requirements += 1
    if need_symbols == 'ДА':
        spisok_vseh_elmentov.extend(punctuation)
        count_of_requirements += 1
    if need_exception == 'ДА':
        for i in range(len(exception)):
            spisok_vseh_elmentov.remove(exception[i])

    if count_of_requirements >= pass_len:
        error = 'Ошибка. Уменьшите количество требований, либо увеличьте длину пароля'
        return error

    for j in range(pass_len - count_of_requirements):  # заполняем пароль случайными символами из общего списка
        user_password.extend(choice(spisok_vseh_elmentov))

    if need_digits == 'ДА':  # дополняем остаток пароля обязательными элементами
        user_password.extend(choice(digits))
    if need_uppers == 'ДА':
        user_password.extend(choice(uppercase_letters))
    if need_lowers == 'ДА':
        user_password.extend(choice(lowercase_letters))
    if need_symbols == 'ДА':
        user_password.extend(choice(punctuation))

    shuffle(user_password)

    return user_password


digits = list('0123456789')
lowercase_letters = list('abcdefghijklmnopqrstuvwxyz')
uppercase_letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
punctuation = list('!#$%&*+-=?@^_')
punctuation_string = '!#$%&*+-=?@^_'
exception = list('il1Lo0O')
exception_string = 'il1Lo0O'

print('Привет. Это программа для создания паролей. Ответь на несколько вопросов и я создам для тебя отличный '
      'безопасныый пароль.')
pass_kolichestvo = int(input('Сколько паролей требуется? : '))
print()
pass_len = int(input('Сколько символов должно быть в пароле? : '))
need_digits = input('В пароле должны быть цифры? (Да/Нет) : ').upper()
need_uppers = input('В пароле должны быть заглавные буквы? (Да/Нет) : ').upper()
need_lowers = input('В пароле должны быть прописные буквы? (Да/Нет) : ').upper()
need_symbols = input(f'Нужно ли включать в пароль следующие символы - {punctuation_string}? (Да/Нет) : ').upper()
need_exception = input(f'Нужно ли исключить из пароля символы {exception_string}? (Да/Нет) : ').upper()

tekushee_kolichestvo = 0
while tekushee_kolichestvo < pass_kolichestvo:
    print(*password_generator(pass_len, need_digits, need_uppers, need_lowers, need_symbols,
                              need_exception),sep='')
    if 'Ошибка' in password_generator(pass_len, need_digits, need_uppers, need_lowers, need_symbols,
                                      need_exception):
        break
    tekushee_kolichestvo += 1


