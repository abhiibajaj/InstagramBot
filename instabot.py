from selenium import webdriver
import os
import time

class InstagramBot:
    def __init__(self, username, password):

        """
        Initialises Instagram Bot object.

        Args:
            username: The Instagram Username 
            password: The Instagram Password

        Attributes:
            driver: Selenium.webdriver.chrome: Used to automate browser actions.
        """
        self.username = username
        self.password = password

        self.driver = webdriver.Chrome("./chromedriver")
       
        self.base_url = "https://www.instagram.com"

        self.login()
        time.sleep(0.3)

        self.follow_user("pokimanelol")
    
    def login(self):
        self.driver.get("{}/accounts/login/".format(self.base_url))
        
        time.sleep(0.2)
        self.driver.find_element_by_name("username").send_keys(self.username)
        self.driver.find_element_by_name("password").send_keys(self.password)
        self.driver.find_element_by_xpath("//div[contains(text(), 'Log In')]").click()

    def nav_user(self, user):
        self.driver.get("{}/{}/".format(self.base_url, user))

    def follow_user(self, user):
        self.nav_user(user)
        follow_button = self.driver.find_element_by_xpath("//button[contains(text(), 'Follow')]")
        follow_button.click()

    def unfollow_user(self, user):
        self.nav_user(user)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Following')]").click()

if __name__ == "__main__":
    ig_bot = InstagramBot("random", "random")

