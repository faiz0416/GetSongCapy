from linebot.models import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from random import choice


def getsong():
    #建立chrome設定
    chromeOption = webdriver.ChromeOptions()
    #設定瀏覽器的user agent
    chromeOption.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0')
    chromeOption.add_argument("start-maximized")
    chromeOption.add_argument('--headless')
    chromeOption.add_argument('--no-sandbox')
    chromeOption.add_argument('--disable-dev-shm-usage')
    #開啟Chrome瀏覽器
    driver = webdriver.Chrome(options=chromeOption)
    #調整瀏覽器視窗大小
    driver.set_window_size(1024, 960)
    
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
