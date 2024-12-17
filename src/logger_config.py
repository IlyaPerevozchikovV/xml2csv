import logging
import os
from datetime import datetime

# Конфигурация логгера
def setup_logger(log_file_name: str, file_path: str):
    """
    setup_logger настраивает логгер, который собирает логи в отдельный файл для каждого XML-файла.
    Принимимает: log_file_name: Имя лог-файла для текущего процесса обработки, file_path путь, по которому
    располагается обрабатываемый XML-файл (Необходим для определения пути создания log-файла)
    Возвращает: Настроенный логгер.
    """
    # Создаём директорию logs, если её нет
    logs_dir = os.path.dirname(file_path) + '\\log\\'
    os.makedirs(logs_dir, exist_ok=True)

    # Полный путь к лог-файлу
    log_file_path = os.path.join(logs_dir, log_file_name)

    # Настройка логгера
    logger = logging.getLogger(log_file_name)  # Создаем уникальный логгер для каждого файла
    logger.setLevel(logging.INFO)  # Устанавливаем уровень логирования

    # Формат записи сообщений
    formatter = logging.Formatter("%(asctime)s | %(levelname)s: %(message)s")

    # Создаём обработчик для записи в файл
    file_handler = logging.FileHandler(log_file_path, encoding="utf-8")
    file_handler.setFormatter(formatter)

    # Добавляем обработчик в логгер
    if not logger.hasHandlers():  # Предотвращаем добавление нескольких обработчиков
        logger.addHandler(file_handler)

    return logger


# Генерация имени лог-файла на основе текущей даты и времени
def generate_log_file_name(file_name: str) -> str:
    """
    Генерирует имя лог-файла на основе имени XML-файла и текущей даты/времени.
    """
    base_name = os.path.splitext(os.path.basename(file_name))[0]
    file_datetime = datetime.now().strftime('%m.%d.%Y')
    return f"{base_name}_{file_datetime}.log"