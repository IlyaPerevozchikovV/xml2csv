import logging

from lxml.etree import XMLParser, parse
from datetime import datetime


def parse_xml(file_path, logger):
    data = []
    encoding = None

    try:
        # Можно не указывать парсер, так как по умолчанию используется XMLPasrser,
        # но в данном случае необходимо установить кодировку (по умолчанию utf-8) поэтому указываем
        parser = XMLParser(encoding='windows-1251')

        with open(file_path, 'rb') as file:          #'rb', так как необходима работа с кодировкой файла
            tree = parse(file, parser)               # Получаем структуру XML-файла в виде "дерева"
            root = tree.getroot()                    # Получаем корень дерева XML-структуры
            encoding = tree.docinfo.encoding

        date: str = tree.findtext('./СлЧаст/ОбщСвСч/ИдФайл/ДатаФайл')  # Получаем дату из XML-файла

        # Получаем данные из необходимых полей XML-файла
        for i, payer in enumerate(root.findall('./ИнфЧаст/Плательщик'), start=1):
            account = payer.findtext('ЛицСч')
            period = payer.findtext('Период')
            fio = payer.findtext('ФИО', "")        # Для неключевых полей fio, address, amount:
            address = payer.findtext('Адрес', "")  # Если не было найдено значение в поле,
            amount = payer.findtext('Сумма', "")   # Записываем пустое значение

            # Обработка отсутствующих полей ключевых значений
            if not account or not period:
                logger.warning(f"Строка {i}: отсутствуют ключевые поля (ЛицСч, Период).")
                continue

            # Обработка некорректного формата периода
            if not period.isdigit() or len(period) != 6:
                logger.warning(f'Строка {i}: некорректный период "{period}".')
                continue


            # Обработка корректности месяца и года в периоде
            try:
                month = int(period[:2])
                year = int(period[2:])
                if month > 12 or month < 1 or year < 1 or year > datetime.now().year:
                    raise ValueError
            except ValueError:
                logger.warning(f'Строка {i}: некорректный период "{period}". Неверное значение месяца/года.')
                continue


            # Обработка некорректных сумм (Отрицательные значения)
            try:
                amount = float(amount)
                if amount <= 0:
                    raise ValueError
            except ValueError:
                logger.warning(f'Строка {i}: некорректная сумма (отрицательное или нулевое значение ) - "{amount}".')
                continue


            # Обработка некорректных сумм (Некорректное значение)
            try:
                amount = round(float(amount), 2)  # Округление до 2 знаков после разделителя
            except ValueError:
                logger.warning(f'Строка {i}: некорректная сумма (некорректный формат данных) - "{amount}".')
                continue


            data.append({
                'file_name': file_path,
                'date': date,
                'account': account,
                'fio': fio,
                'address': address,
                'period': period,
                'amount': amount
            })

        logger.info(f"Данные из XML-файла были успешно собраны.")

    except Exception as error:
        logger.error(f'Ошибка обработки файла {file_path}: {error}')

    return data, encoding