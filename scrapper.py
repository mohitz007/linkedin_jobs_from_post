from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
from selenium.webdriver.chrome.options import Options


import log as login
username = login.username
password = login.password

def scrapper():

    def scroll_down():
        """A method for scrolling the page."""
        Time = time.time()
        scrollTime=100
        # Get scroll height.
        last_height = driver.execute_script("return document.body.scrollHeight")

        while Time+scrollTime>time.time():

            # Scroll down to the bottom.
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load the page.
            time.sleep(0.8)

            # Calculate new scroll height and compare with last scroll height.
            new_height = driver.execute_script("return document.body.scrollHeight")

            if new_height == last_height:

                break

            last_height = new_height

    # options = Options()
    # options.headless = True
    driver = webdriver.Chrome()
    driver.get("https://www.linkedin.com/")
    driver.find_element_by_id("session_key").send_keys(username)
    driver.find_element_by_id("session_password").send_keys(password+'\n')
    time.sleep(10)  #to wait for linkedin to load
    try:
        scroll_down()
        delay = 15 #time to wait for elements to appear
        myElem = WebDriverWait(driver, delay).until(lambda x: x.find_elements_by_xpath("//div[contains(@id,'ember')]/span/span/span"))
        sourceFile = open('data.txt', 'w')
        for ele in myElem:
            print((ele.text + ' ').encode('utf-8'),file=sourceFile)
        sourceFile.close()
        print( "Page is ready!")

        
    except TimeoutException:
        print("Loading took too much time!")