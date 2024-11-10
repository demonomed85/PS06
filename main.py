from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
from selenium.webdriver.firefox.options import Options

url = 'https://www.divan.ru/'

options = Options()
options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0")
site = webdriver.Firefox(options=options)
#site = webdriver.Chrome()

try:
    site.get(url)
    print(site)


    try:
        cards = WebDriverWait(site, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'lsooF')))
        print(f"Найдено {len(cards)} элементов с классом 'lsooF'")

        for card in cards:
            print(card.text)

    except TimeoutException:
        print("Время ожидания истекло: элементы не были найдены.")
    except NoSuchElementException:
        print("Элементы не найдены на странице.")

except WebDriverException as e:
    print(f"Ошибка веб-драйвера: {e}")

finally:
    site.quit()