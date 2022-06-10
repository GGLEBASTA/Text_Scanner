import pytesseract
from PIL import Image

""" Python-tesseract - это инструмент оптического распознавания символов (OCR) для python.
    OCR Engine Mode (--oem) (режим работы "движка" распознавания символов);
        Page Segmentation Mode (--psm) (режим сегментации страниц)."""

#Открываем изображение
IMG = Image.open('')

#Вытаскиваем название файла с изображением для дальнейшего его использования
file_name = IMG.filename
file_name_1 = file_name.split(".")[0]

#Пользовательская конфигурация oem/psm (смотреть документацию/настраивать под себя)
custom_oem_psm_config = r'--oem 3 --psm 13'

#Путь до tessetact.exe на вашем ПК
pytesseract.pytesseract.tesseract_cmd = ''

#Переводим картинку с текстом в строку с информацией,также добавив конфиг для лучшего считывания информации
text = pytesseract.image_to_string(IMG,config=custom_oem_psm_config)

#Запись результата сканирования в файл,именуемый как и само изображение
with open(f'{file_name_1}.txt','w') as f:
    f.write(text)

