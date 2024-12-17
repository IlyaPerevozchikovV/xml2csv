import sys
import os

from src.file_processor import process_file, move_to_dir
from src.logger_config import setup_logger, generate_log_file_name


def main():
    # Проверяем, верно ли передана команда в командную строку
    if len(sys.argv) != 2:
        print("Не были получены корректные аргументы!\nИспользование: python main.py <file_name>")     #############
        sys.exit(1)

    file_path = sys.argv[1]

    # Проверяем, суещствует ли файл с переданным именем, и является ли он файлом
    if not os.path.isfile(file_path):
        print(f"Ошибка: файл '{file_path}' не найден")                    ########################
        sys.exit(1)

    # Проверяем расширение файла
    if not file_path.lower().endswith('.xml'):
        print(f"Файл не является XML-файлом")                   ########################
        move_to_dir(file_path, status='bad')
        sys.exit(1)

    # Генерация имени log-файла
    log_file_name = generate_log_file_name(file_path)
    logger = setup_logger(log_file_name, file_path)

    # Вызываем функцию обработки файла после успешного прохождения проверок
    process_file(file_path, logger)


if __name__ == "__main__":
    main()
