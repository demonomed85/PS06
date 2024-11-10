from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
from selenium.webdriver.firefox.options import Options
import csv

url = 'https://www.divan.ru/category/svet'

options = Options()
options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0")
#site = webdriver.Firefox(options=options)
site = webdriver.Chrome()

try:
    site.get(url)
    #print(site)

    cards = []

    try:
        all_goods = WebDriverWait(site, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'lsooF')))
        print(f"Найдено {len(cards)} элементов с классом 'lsooF'")

        for good in all_goods:
            name = good.find_element(By.CSS_SELECTOR, 'span').text
            price = good.find_element(By.CSS_SELECTOR, 'span.ui-LD-ZU').text
            url = good.find_element(By.CSS_SELECTOR, 'a.ui-GPFV8').get_attribute('href')

            cards.append([name, price, url])
            #print(name,price, url)

        # Прописываем открытие нового файла, задаём ему название и форматирование
        # 'w' означает режим доступа, мы разрешаем вносить данные в таблицу
        with open("lights.csv", 'w', newline='', encoding='windows-1251') as file:
            # Используем модуль csv и настраиваем запись данных в виде таблицы
            # Создаём объект
            writer = csv.writer(file)
            # Создаём первый ряд
            writer.writerow(['Наименование товара', 'Цена', 'Ссылка'])
            # Прописываем использование списка как источника для рядов таблицы
            writer.writerows(cards)

        print("Данные успешно записаны в таблицу.")

    except TimeoutException:
        print("Время ожидания истекло: элементы не были найдены.")
    except NoSuchElementException:
        print("Элементы не найдены на странице.")

except WebDriverException as e:
    print(f"Ошибка веб-драйвера: {e}")

finally:
    site.quit()