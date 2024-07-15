def custom_write(file_name, strings):
    strings_positions = {}
    with open(file_name, 'w', encoding='utf-8') as file:
        for index, string in enumerate(strings, start=1): # Нумеруем строки
            byte_position = file.tell() # Перед записью каждой строки использую метод tell() для получения текущей позиции в байтах
            file.write(string + '\n') # Каждая запись с новой строки
            strings_positions[(index, byte_position)] = string # [записали ключ] = значение
        return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)