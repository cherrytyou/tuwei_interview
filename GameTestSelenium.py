from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time

# 设置 Chrome 选项
chrome_options = Options()
chrome_options.add_argument("--headless")  # 无头模式
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("window-size=1920,1080")

# 创建 WebDriver 实例
driver = webdriver.Chrome(options=chrome_options)

try:
    # 打开游戏网页
    driver.get("https://h5.g123.jp/game/jya?lang=zh-TW")

    # 等待页面加载
    time.sleep(5)

    # 查找并打印页面标题
    page_title = driver.title
    print("页面标题：", page_title)

    # 检查标题是否与预期匹配
    expected_title = "小邪神飛踢 混沌 | 開始遊戲 - G123"
    if page_title == expected_title:
        print("页面标题匹配！")
    else:
        print("页面标题不匹配！")

        # 查找并点击开始游戏按钮
    # start_button = driver.find_element(By.XPATH, '//button[contains(text(),"開始遊戲")]')  # 根据实际文本修改
    # print("找到的按钮文本：", start_button.text)
    #
    # # 点击按钮
    # start_button.click()
    #
    # # 等待游戏加载
    # time.sleep(10)  # 根据实际情况进行调整
    #
    # # 进一步与游戏元素交互
    # # 示例: 可以查找游戏中的元素并进行交互
    #
    # # 等待观察结果
    # time.sleep(3)

finally:
    # 关闭浏览器
    driver.quit()