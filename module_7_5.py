import os
import time

print(f'Изменение рабочей директории:')
module = os.getcwd()
print(f'Путь до изменения: {module}')
os.mkdir(r"D:\Python\folder") # создаём директорию
os.chdir(r"D:\Python\folder") # меняем директорию
module_2 = os.getcwd()
print(f'Путь после изменения: {module_2}')
os.chdir(r"D:\Python\Module_7") # возвращаем обратно
print(os.getcwd())

print(f'\nПрименение os.walk:')
os.makedirs(r"D:\Python\folder\first\second") # создаём директории
file_path = r"D:\Python\folder\new_file.txt" # создаём файл
with open(file_path, 'w') as file:
    file.write('Выполнение домашнего задания. Модуль 7_5')
for root, directories, files in os.walk(r"D:\Python\folder"):
    for directory in directories:
        print(f'Обнаружена директория: {directory}')
    for file in files:
        filepath = os.path.join(root, file)
        # filesize = os.stat(os.path.join(root, file)).st_size # альтернатива
        filesize = os.path.getsize(os.path.join(root, file))
        # filetime = os.stat(os.path.join(root, file)).st_mtime   # альтернатива
        filetime = os.path.getmtime(os.path.join(root, file))
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        parent_dir = os.path.dirname(os.path.join(root, file))
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, '
              f'Родительская директория: {parent_dir}')