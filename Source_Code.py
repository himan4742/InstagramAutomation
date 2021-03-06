from Config_File import name, passW

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException, NoSuchElementException

#name = input("Enter your username - ")
#passW = input("Enter your password - ")


class Insta_Login(object):
    """."""

    INSTAGRAM_URL = "https://www.instagram.com/"
    BROWSER_WINDOW_DIMENSIONS = {'width': 1920, 'height': 1080}

    driver = webdriver.Chrome(executable_path="C://Users/Himanshu/Downloads//chromedriver.exe")

    def __init__(self, name, passW):
        """."""

        self.name = name
        self.passW = passW

    def login(self):
        """."""

        try:
            username = WebDriverWait(self.driver, 10).until(
                expected_conditions.visibility_of_element_located(
                    (By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')))
        except TimeoutException:
            self.login()
        else:
            username.send_keys(self.name)
            password = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
            password.send_keys(self.passW)
            self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]').click()
            self.skip_notification()

    def skip_notification(self):
        """."""

        not_now = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button')))
        not_now.click()

        notification_not_now = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, '/ html / body / div[4] / div / div / div / div[3] / button[2]')))
        notification_not_now.click()

    def search(self):
        """."""

        try:
            search_element = WebDriverWait(self.driver, 5).until(
                expected_conditions.visibility_of_element_located(
                    (By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div/div')))
        except TimeoutException:
            self.search()
        else:
            search_query = input("Enter your search - ")
            search_element.click
            search_element2 = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
            search_element2.send_keys(search_query)
            search_element2.click()

    def _go_to_settings(self):
        """."""

        try:
            option = WebDriverWait(self.driver, 10).until(
                    expected_conditions.visibility_of_element_located(
                        (By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img')))
        except (TimeoutException, NoSuchElementException):
            self._go_to_settings()
        else:
            option.click()
            setting_option = WebDriverWait(self.driver, 10).until(
                expected_conditions.visibility_of_element_located(
                    (By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/a[3]/div')))
            setting_option.click()

    def logout(self):
        """."""

        try:
            option = WebDriverWait(self.driver, 10).until(
                    expected_conditions.visibility_of_element_located(
                        (By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img')))
        except (TimeoutException, NoSuchElementException):
            self.logout()
        else:
            option.click()
            logout = WebDriverWait(self.driver, 20).until(
                    expected_conditions.visibility_of_element_located(
                        (By.CSS_SELECTOR, '#f992869cc4a5f8 > div > div > div')))
            logout.click()

    def parse(self):
        """."""

        self.driver.set_window_size(**self.BROWSER_WINDOW_DIMENSIONS)
        self.driver.get(self.INSTAGRAM_URL)
        self.login()
        #self.search()
        self.logout()
        self._go_to_settings()


himanshu = Insta_Login(name, passW)
Insta_Login.parse(himanshu)
