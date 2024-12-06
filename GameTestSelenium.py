import os
import shutil
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# 指定驱动目标位置
folder_path = r'C:\Users\Abby\PycharmProjects\pythonProject\venv\Scripts'
file_path = os.path.join(folder_path, 'chromedriver.exe')
download_driver_path = ChromeDriverManager().install()
shutil.copy(download_driver_path, folder_path)
driver = webdriver.Chrome(service=Service(file_path))
driver.get("https://h5.g123.jp/game/jya?lang=zh-TW")
