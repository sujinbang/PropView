from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
import os
import time
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
import sys

chrome_options = ChromeOptions()
driver = None # driver 변수 초기화

try:
    driver = webdriver.Chrome(options=chrome_options)

except Exception as e:
    print(f"Error initializing ChromeDriver: {e}")

driver.get('https://land.naver.com/')
time.sleep(10)  # 페이지 로드 대기