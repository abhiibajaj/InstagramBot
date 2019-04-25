from selenium import webdriver
import os
import time

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password

        self.driver = webdriver.Chrome("./chromedriver")
        self.login()
    
    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        
        time.sleep(0.2)
        self.driver.find_element_by_name("username").send_keys(self.username)
        self.driver.find_element_by_name("password").send_keys(self.username)

        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[5]/button/div').click()


if __name__ == "__main__":
    ig_bot = InstagramBot("temp_username", "temp_password")
