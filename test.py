import scrapper

scrapper.scrapper()


# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import TimeoutException

# driver = webdriver.Chrome()
# driver.get("http://127.0.0.1/Corona-management-system/feed.html")
# # x=driver.find_element_by_css_selector("div[id^='ember']")
# x=driver.find_elements_by_xpath("//div[contains(@id,'ember')]/span/span/span")
# for ele in x:
#     print(ele.text)
# print((ele.text + '\n').encode('utf-8'),file=sourceFile)