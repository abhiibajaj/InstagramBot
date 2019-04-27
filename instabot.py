from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import os
import time
import configparser

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

    
    def login(self):
        self.driver.get("{}/accounts/login/".format(self.base_url))
        
        time.sleep(0.2)
        self.driver.find_element_by_name("username").send_keys(self.username)
        self.driver.find_element_by_name("password").send_keys(self.password)
        self.driver.find_element_by_xpath("//div[contains(text(), 'Log In')]").click()
        time.sleep(1.2)


    def nav_user(self, user):
        self.driver.get("{}/{}/".format(self.base_url, user))
        time.sleep(0.2)


    def follow_user(self, user):
        self.nav_user(user)
        follow_button = self.driver.find_element_by_xpath("//button[contains(text(), 'Follow')]")
        follow_button.click()

    def unfollow_user(self, user):
        self.nav_user(user)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Following')]").click()
    
    def like_all_photos(self, user):

        self.nav_user(user)
        time.sleep(2)
        # action_chains = ActionChains(self.driver)
        # # action_chains.double_click(image).perform()
        # image = self.driver.find_element_by_css_selector("div article div div div div a div")
        images = self.driver.find_elements_by_css_selector("div article div div div div a:nth-child(1)")
        print(len(images))
        for image in images:
            self.like_photo(image)
            time.sleep(1)
        
    def like_photo(self, image):

        image.click()
        time.sleep(1.5)
        # like_button = self.driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/article/div[2]/section[1]/span[1]/button")
        # like_button.click()

        exit_button = self.driver.find_element_by_xpath("/html/body/div[3]/button[1]")
        exit_button.click()

if __name__ == "__main__":
    config = './config.ini'
    cparser = configparser.ConfigParser()
    cparser.read(config)

    username = cparser["AUTH"]["User"]
    password = cparser["AUTH"]["Pass"]

    ig_bot = InstagramBot(username, password)
    ig_bot.like_all_photos("Undertaker")

