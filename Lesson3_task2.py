#Пользователь вводит 3 числа, найти среднее арифмитическое с точность 3

number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))
number_3 = int(input('Введите третье число: '))
average = round((number_1 + number_2 + number_3)/3,3)
print('Среднее арифметическое = ' + str(average))


