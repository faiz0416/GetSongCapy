from linebot.models import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from random import choice
import os

def getsong():
    
    for i in range(2):
        if i == 0:
            url1 = 'https://open.spotify.com/'
            classname1 = 'tsv7E_RBBw6v0XTQlcRo'
            classname2 = 'Nqa6Cw3RkDMV8QnYreTr'
        else:
            url1 = onesong
            classname1 = 'HcMOFLaukKJdK5LfdHh0'
            classname2 = 't_yrXoUO3qGsJS4Y6iXX'
        
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        chrome_options.add_argument("--headless") #無頭模式
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

        driver.get(url1)

        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, classname1)))

        songs = driver.find_elements(By.CLASS_NAME, classname2)

        list_song = []

        for song in songs:
            if song.get_attribute('href') != None:
                list_song.append(str(song.get_attribute('href')))

        onesong = choice(list_song)
        driver.quit()
        
    return onesong
   
    
