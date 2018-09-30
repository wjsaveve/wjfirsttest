from selenium import webdriver

dr1 = webdriver.Firefox()
dr1.get("http://www.baidu.com")

dr2 = webdriver.Ie()
dr2.get("http://www.baidu.com")

dr3 = webdriver.Chrome()
dr3.get("http://www.baidu.com")