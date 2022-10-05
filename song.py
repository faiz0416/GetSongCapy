from linebot.models import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from random import choice
import os

def getsong():

    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless") #無頭模式
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    
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
