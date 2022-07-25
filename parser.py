from random import choice, randint
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from random_word import RandomWords


def create_url():
    r = RandomWords()

    word = r.get_random_word()
    url = 'https://www.google.kz/search?q=' + word + '%20' + '&tbm=isch&hl=ru&tbs=isz:i&authuser=0&sa=X&ved=0CAQQpwVqFwoTCKipyraR0PYCFQAAAAAdAAAAABAC&biw=1491&bih=751'
    return url

def get_html():

    options = Options()
    options.headless = True
    driver = webdriver.Chrome('./chromedriver_win32/chromedriver.exe', options=options)

    # driver.maximize_window()
    # driver.set_window_size(500, 500)
    try:
        driver.get(url=create_url())
        time.sleep(0.5)

        SCROLL_PAUSE_TIME = 0.1

        # Get scroll height
        last_height = driver.execute_script("return document.body.scrollHeight")

        time_for_web = 0
        while True:
            # Scroll down to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            time.sleep(1)

            try:
                driver.find_element(by=By.CLASS_NAME, value='r0zKGf').click()
            except Exception as _ex:
                pass

            try:
                driver.find_element(by=By.CLASS_NAME, value='mye4qd').click()
            except Exception as _ex:
                pass

            if driver.find_element(by=By.CLASS_NAME, value='OuJzKb.Bqq24e').text == "Больше ничего нет":
                time_for_web = time_for_web + 1

            if time_for_web == 2:
                print(driver.find_element(by=By.CLASS_NAME, value='OuJzKb.Bqq24e').text)
                with open("./page_html.html", "w", encoding="utf-8") as file:
                    file.write(driver.page_source)
                break
    except Exception as _ex:
        print(_ex)
    finally:
        driver.close()
        driver.quit()
    pass



def get_urls_from_html():
    get_html()
    with open("./page_html.html", "r", encoding="utf-8") as html:
        soup = BeautifulSoup(html, "html.parser")
        images = soup.find_all('img',{"src":True})
        ready_images = set()
        for image in images:
            ready_images.add(image['src'])
    return list(ready_images)


if __name__ == "__main__":
    get_urls_from_html()