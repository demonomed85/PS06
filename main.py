import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
import time
import csv

url = 'https://www.divan.ru/'
site = webdriver.Firefox()

try:
    site.get(url)
    time.sleep(3)
    print('1')
    cards = site.find_elements(By.CLASS_NAME, 'lsooF')
    print(len(cards))

#    for card in cards:
#       print(card.text)

except TimeoutException:
    print("Время ожидания истекло: элементы не были найдены.")
except NoSuchElementException:
    print("Элементы не найдены на странице.")
except WebDriverException as e:
    print(f"Ошибка веб-драйвера: {e}")
finally:
    site.quit()
