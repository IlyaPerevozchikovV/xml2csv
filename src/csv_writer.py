import csv
import os
import logging


def write_csv(data: list[dict], csv_path: str, encoding: str, logger) -> None:
    """
    Создает и записывает CSV-файл в той же директории, что и XML-файл.
    :параметр data: Список словарей, содержащих данные для записи.
    :параметр csv_path: Полный путь к исходному XML-файлу.
    :параметр encoding: Кодировка файла (по умолчанию "utf-8").
    """
    try:
        # Создаем csv-файл для записи
        with open(csv_path, mode='w', newline='', encoding=encoding) as file:
            writer = csv.writer(file, delimiter=';')
            logger.info(f'CSV-файл {os.path.basename(csv_path)} был успешно создан в {os.path.dirname(csv_path)}')

            # Запись данных в CSV-файл
            for element in data:
                writer.writerow([
                    element.get('file_name'),
                    element.get('date'),
                    element.get('account'),
                    element.get('fio', ''),
                    element.get('address', ''),
                    element.get('period'),
                    element.get('amount', '')
                ])

            logger.info(f"Данные были успешно записаны в {os.path.basename(csv_path)}")

        logger.info(f"CSV файл сохранен по пути: {csv_path}")

    except Exception as e:
        logging.error(f"Ошибка при создании CSV-файла: {e}")