from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


PATH = "chromedriver.exe"
URL = 'https://www.google.com'
request = 'Python разработчик'
service = Service(PATH)
driver = webdriver.Chrome(service=service)


def main():
    heads = []
    urls = []
    driver.get(URL)
    driver.find_element(By.NAME, 'q').send_keys(request + Keys.RETURN)
    elements = driver.find_elements(By.CLASS_NAME, "yuRUbf")
    for elem in elements:
        head = elem.find_element(By.TAG_NAME, "h3").text
        url = elem.find_element(By.TAG_NAME, "a").get_attribute("href")
        if url != "" and head != "":
            heads.append(head)
            urls.append(url)

    for i in range(0, 5):
        print(heads[i])
        print(urls[i])

    time.sleep(5)
    driver.close()
    driver.quit()


if __name__ == "__main__":
    main()
