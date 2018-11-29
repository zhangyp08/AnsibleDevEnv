from selenium import webdriver
import time

dr = webdriver.Chrome()
url = 'https://www.baidu.com' #it will fail if input 'www.baidu.com'
dr.get(url)
time.sleep(3)
print(dr.title)

dr.find_element_by_id("kw").clear()
dr.find_element_by_id("kw").send_keys("python自动化测试")
dr.find_element_by_id("su").click()

try:
    assert "百度一下，你就知道" in dr.title
    print("Test PASS")
except Exception as e:
    print("Test Fail")

dr.quit()
