#Импортируем метод sample для получения нескольких случайных значений из списка
from random import sample
#Функция получения случайных значений из списка
def generate_password(length, chars):
    return ''.join(sample(chars, length))

chars = []
pwd_quantity = int(input('Сколько паролей вам нужно сгенерировать? '))
pwd_len = int(input('Какой длины должен быть пароль? '))
if input('Включать ли в пароль цифры от 0 до 9? ').lower() == 'да':
    chars += list('0123456789')
if input('Включать ли в пароль прописные буквы? ').lower() == 'да':
    chars += list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
if input('Включать ли в пароль строчные буквы? ').lower() == 'да':
    chars += list('abcdefghijklmnopqrstuvwxyz')
if input('Включать ли в пароль символы "!#$%&*+-=?@^_"? ').lower() == 'да':
    chars += list('!#$%&*+-=?@^_')
if input('Исключать ли неоднозначные символы "il1Lo0O"? ').lower() == 'да':
    for i in ('il1Lo0O'):
        if i in chars:
            chars.remove(i)
for i in range(pwd_quantity):
    print(generate_password(pwd_len, chars))
