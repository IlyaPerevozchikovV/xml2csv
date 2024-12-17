import os
import shutil
import logging


# Функция перемещения некорректных/корректных файлов в соответствующую директорию
def move_to_dir(file_path, directory_name):
    directory = os.path.join(os.path.dirname(file_path), directory_name)
    os.makedirs(directory, exist_ok=True)
    shutil.move(os.path.join(os.path.dirname(file_path), os.path.basename(file_path)), directory)
    logging.info(f'Файл {os.path.basename(file_path)} был успешно перемещен в {directory}.')