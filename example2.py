def validate_user_input(data):
    try:
        if not isinstance(data, dict):
            raise TypeError("Ошибка: ожидается словарь.")
    except TypeError as e:
        print(e)
        return  # Завершаем выполнение функции для некорректного типа данных
    
    try:
        if 'name' in data and isinstance(data['name'], str):
            print("Ключ 'name' присутствует, и его значение - строка.")
        else:
            raise ValueError("Ошибка: либо ключ 'name' отсутствует, либо его значение не является строкой.")
    except ValueError as e:
        print(e)
        return  # Завершаем выполнение функции при ошибке ключа 'name'
    
    try:
        if 'age' in data and isinstance(data['age'], (int, float)) and data['age'] > 0:
            print("Ключ 'age' присутствует и является положительным числом.")
        else:
            raise ValueError("Ошибка: либо ключ 'age' отсутствует, либо его значение не является положительным числом.")
    except ValueError as e:
        print(e)
        return  # Завершаем выполнение функции при ошибке ключа 'age'

# Тестируем вызовы
validate_user_input({"name": "Alice", "age": 30})
print('-------------------------\n')
validate_user_input({"age": 12})
print('-------------------------\n')
validate_user_input({"name": "Nata", "age": -6})
print('-------------------------\n')
validate_user_input("dict for value")
print('-------------------------\n')

