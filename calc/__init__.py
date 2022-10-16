import div
import mult
import sub
import sum
import complex
import exceptions as ex
import log as lg

more_log = []


def button_click():
    type_of_number = 0
    while not type_of_number:
        print('1. Рациональные')
        print('2. Комплексные')
        print('3. Выход\n')
        print('С какими числами будем работать?')
        type_of_number = ex.type_of_number()

        if type_of_number == 1:
            print('1. Сложение')
            print('2. Вычитание')
            print('3. Деление')
            print('4. Целочисленное деление')
            print('5. Остаток от деление')
            print('6. Умножение')
            print('7. Возведение в степень')
            print('8. Извлечение корня\n')
            print('Какую операцию будем производить?')
            operation = ex.operation()

            if operation == 1:
                print('Введите первое значение: ')
                a = ex.number()
                print('Введите второе значение: ')
                b = ex.number()
                result = sum.sum(a, b)
                print('Сумма равна: ', result)
                op = 'Сложение'
            elif operation == 2:
                print('Введите первое значение: ')
                a = ex.number()
                print('Введите второе значение: ')
                b = ex.number()
                result = sub.sub(a, b)
                print('Разность равна: ', result)
                op = 'Вычитание'
            elif operation == 3:
                print('Введите первое значение: ')
                a = ex.number()
                print('Введите второе значение: ')
                b = ex.number()
                result = div.div(a, b)
                print('Частное равно: ', result)
                op = 'Деление'
            elif operation == 4:
                print('Введите первое значение: ')
                a = ex.number()
                print('Введите второе значение: ')
                b = ex.number()
                result = div.int_div(a, b)
                print('Частное от целочисленного деления равно: ', result)
                op = 'Целочисленное деление'
            elif operation == 5:
                print('Введите первое значение: ')
                a = ex.number()
                print('Введите второе значение: ')
                b = ex.number()
                result = div.rem_of_div(a, b)
                print('Остаток от деления равен: ', result)
                op = 'Остаток от деления'
            elif operation == 6:
                print('Введите первое значение: ')
                a = ex.number()
                print('Введите второе значение: ')
                b = ex.number()
                result = mult.mult(a, b)
                print('Произведение равно: ', result)
                op = 'Умножение'
            elif operation == 7:
                print('Введите первое значение: ')
                a = ex.number()
                print('Введите второе значение: ')
                b = ex.number()
                result = mult.pow(a, b)
                print(f'{a} в степени {b} равно: {result}')
                op = 'Возведение в степень'
            elif operation == 8:
                print('Введите значение: ')
                a = ex.number()
                b = 0.5
                result = mult.mult(a, b)
                print('Квадратный корень равен: ', result)
                op = 'Извлечение квадратного корня'
            else:
                print('Такой операции не существует.')
            for_log = [op, a, b, result]

        elif type_of_number == 2:
            print('1. Сложение')
            print('2. Вычитание')
            print('3. Деление')
            print('4. Умножение')
            print('5. Возведение в степень')
            print('6. Извлечение корня')
            print('Какую операцию будем производить?')
            operation = ex.operation()

            if operation == 1:
                print('Введите реальную часть первого числа: ')
                a1 = ex.number()
                print('Введите мнимую часть первого числа: ')
                a2 = ex.number()
                a = complex.comp(a1, a2)
                print('Введите реальную часть второго числа: ')
                b1 = ex.number()
                print('Введите мнимую часть второго числа: ')
                b2 = ex.number()
                b = complex.comp(b1, b2)
                result = sum.sum(a, b)
                print('Сумма равна: ', result)
                op = 'Сложение'
            elif operation == 2:
                print('Введите реальную часть первого числа: ')
                a1 = ex.number()
                print('Введите мнимую часть первого числа: ')
                a2 = ex.number()
                a = complex.comp(a1, a2)
                print('Введите реальную часть второго числа: ')
                b1 = ex.number()
                print('Введите мнимую часть второго числа: ')
                b2 = ex.number()
                b = complex.comp(b1, b2)
                result = sub.sub(a, b)
                print('Разность равна: ', result)
                op = 'Вычитание'
            elif operation == 3:
                print('Введите реальную часть первого числа: ')
                a1 = ex.number()
                print('Введите мнимую часть первого числа: ')
                a2 = ex.number()
                a = complex.comp(a1, a2)
                print('Введите реальную часть второго числа: ')
                b1 = ex.number()
                print('Введите мнимую часть второго числа: ')
                b2 = ex.number()
                b = complex.comp(b1, b2)
                result = div.div(a, b)
                print('Частное равно: ', result)
                op = 'Деление'
            elif operation == 4:
                print('Введите реальную часть первого числа: ')
                a1 = ex.number()
                print('Введите мнимую часть первого числа: ')
                a2 = ex.number()
                a = complex.comp(a1, a2)
                print('Введите реальную часть второго числа: ')
                b1 = ex.number()
                print('Введите мнимую часть второго числа: ')
                b2 = ex.number()
                b = complex.comp(b1, b2)
                result = mult.mult(a, b)
                print('Произведение равно: ', result)
                op = 'Умножение'
            elif operation == 5:
                print('Введите реальную часть первого числа: ')
                a1 = ex.number()
                print('Введите мнимую часть первого числа: ')
                a2 = ex.number()
                a = complex.comp(a1, a2)
                b = int(input('Введите значение степени: '))
                result = mult.pow(a, b)
                print(f'{a} в степени {b} равно: {result}')
                op = 'Возведение в степень'
            elif operation == 6:
                print('Введите реальную часть первого числа: ')
                a1 = ex.number()
                print('Введите мнимую часть первого числа: ')
                a2 = ex.number()
                a = complex.comp(a1, a2)
                b = 0.5
                result = mult.mult(a, b)
                print('Квадратный корень равен: ', result)
                op = 'Извлечение квадратного корня'
            else:
                print('Такой операции не существует.')
            for_log = [op, a, b, result]

        elif type_of_number == 3:
            break

        else:
            print('Такого номера нет в списке.')

        more_log.append(for_log)

    return (more_log)