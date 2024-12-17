# XML-to-CSV Converter
___________________________________________________________________________________
Эта программа реализует преобразование XML-файла с реестром начислений в CSV-формат.
Реализована фильтрация некорректных данных в ключевых и неключевых значениях.

# Требования
- python 3.6+
- pip

# Инструкция для запуска

  **Клонируйте репозиторий:**
```bash  
git clone https://github.com/IlyaPerevozchikovV/xml2csv.git
cd xml2csv
```
  **Создайте виртуальное окружение и активируйте его:**

Для Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
```
Для Linux/macOS
```bash      
source .venv/bin/activate
source .venv/bin/activate
```
  **Установите зависимости:**
  ```bash
pip install -r requirements.txt
```
  **Использование:**
  ```bash
python main.py path_to_xml_file
```
