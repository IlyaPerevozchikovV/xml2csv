from src.csv_writer import write_csv
from src.xml_parser import parse_xml

import os
import shutil
import logging


# Функция обработки валидного файла
def process_file(file_path: str, logger):
    file_directory = os.path.dirname(file_path)  # Сохраняем путь к файлу
    file_name = os.path.basename(file_path)  # Сохраняем название самого файла

    try:
        data, encoding, issues = parse_xml(file_path, logger)
        if issues:
            for issue in issues:
                logger.warning(issue)

        csv_path = os.path.join(file_directory, file_name.replace('.xml', '.csv'))
        write_csv(data, csv_path, encoding, logger)
        logger.info(f'Файл {file_name} успешно обработан.')
        print(f'Файл {file_name} успешно обработан.')
        move_to_dir(file_path, status='good')

    except Exception as error:
        logging.error(f'Ошибка обработки файла {file_name}: {error}.')


# Функция перемещения некорректных/корректных файлов в соответствующую директорию
def move_to_dir(file_path, status):
    if status == 'bad':
        bad_dir = os.path.dirname(file_path)+'\\bad\\'
        os.makedirs(bad_dir, exist_ok=True)
        shutil.move(os.path.join(os.path.dirname(file_path), os.path.basename(file_path)), bad_dir)
        logging.info(f'Файл {os.path.basename(file_path)} был успешно перемещен в {bad_dir}.')

    if status == 'good':
        arh_dir = os.path.dirname(file_path)+'\\arh\\'
        os.makedirs(arh_dir, exist_ok=True)
        shutil.move(os.path.join(os.path.dirname(file_path), os.path.basename(file_path)), arh_dir)
        logging.info(f'Файл {os.path.basename(file_path)} был успешно перемещен в {arh_dir}.')

    return None