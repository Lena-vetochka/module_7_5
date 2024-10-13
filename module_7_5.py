import os, time
directory = '.'

for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)                  #полный путь к файлам
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))  #время последнего изменения
        filesize = os.path.getsize(filepath)                 #размер файла
        parent_dir = os.path.dirname(filepath)               #родительская директория
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, '
              f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')

        