import sys
import os

from src.move_to_dir import move_to_dir
from src.logger_config import setup_logger, generate_log_file_name
from src.csv_writer import write_csv
from src.xml_parser import parse_xml



def main():
    # Проверяем, верно ли передана команда в командную строку
    if len(sys.argv) != 2:
        print("Не были получены корректные аргументы!\nИспользование: python main.py <file_name>")
        sys.exit(1)

    file_path = sys.argv[1]

    # Проверяем, существует ли файл с переданным именем, и является ли он файлом
    if not os.path.isfile(file_path):
        print(f"Ошибка: файл '{file_path}' не найден")
        sys.exit(1)

    # Проверяем расширение файла
    if not file_path.lower().endswith('.xml'):
        print(f"Файл не является XML-файлом")
        move_to_dir(file_path, directory_name='bad')
        sys.exit(1)

    # Вызов функции настройки логирования
    logger = setup_logger(file_path)

    # Сохраняем имя файла и имя директории по-отдельности
    file_directory = os.path.dirname(file_path)
    file_name = os.path.basename(file_path)

    # Вызываем функции обработки файла после успешного прохождения проверок
    try:
        data, encoding = parse_xml(file_path, logger)
        csv_path = os.path.join(file_directory, file_name.replace('.xml', '.csv'))
        write_csv(data, csv_path, encoding, logger)
        move_to_dir(file_path, directory_name='arh')

    except Exception as error:
        logging.error(f'Ошибка обработки файла {file_name}: {error}.')


if __name__ == "__main__":
    main()
