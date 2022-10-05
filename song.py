from linebot.models import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from random import choice


def getsong():
    PATH = 'chromedriver.exe'
    options = webdriver.ChromeOptions()

    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')

    options.add_experimental_option(
        "excludeSwitches", ['enable-automation', 'enable-logging'])
    wd_path = "C:/Users/faiz0/OneDrive/桌面/chromedriver_win32/chromedriver.exe"

    driver = webdriver.Chrome(PATH,chrome_options=options)
    size_Dict = driver.get_window_size()

    driver.get(
        'https://www.youtube.com/watch?v=23g5HBOg3Ic&list=RDCLAK5uy_mOmfogvkugBD9vd5EbejT2y82WidC6as0&start_radio=1')

    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located(
            (By.ID, 'video-title'))
    )

    songs = driver.find_elements(By.ID, 'wc-endpoint')
    list_song = []
    # video-title   wc-endpoint

    for song in songs:
        list_song.append(str(song.get_attribute('href')))

    onesong = choice(list_song)

    print(onesong)

    time.sleep(2)
    driver.quit()
    return onesong
