def convert_to_int(value):
    try:
        result = int(value)
    except ValueError:
        # обработка исключения
        print(f'Преобразование {value} в целое число не возможно.')
    except TypeError:
        print(f'Произошла неожиданная ошибка!') 
    else:
        print(f'Результат преобразования = {result}')
    finally:
        print(f'Работа функции преобразования завершена.')

convert_to_int(input('Введите число: '))
convert_to_int(input('Введите число: '))
convert_to_int([1,2,3])
print("________________________________")