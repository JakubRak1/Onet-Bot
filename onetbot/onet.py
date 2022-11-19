import os

from selenium.webdriver.common.by import By
from onetbot.constant import URL_for_email
from selenium import webdriver


class Onet(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\Selenium", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        option = webdriver.ChromeOptions()
        option.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(Onet, self).__init__(options=option)
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def load_first_page(self):
        self.get(URL_for_email)

    def accept_cookies(self):
        accept_cookie_btn = self.find_element(
            By.CSS_SELECTOR, 'button[aria-label="accept and close"]'
        )
        accept_cookie_btn.click()

    def go_to_login_section(self):
        login_btn = self.find_element(By.CSS_SELECTOR, 'a[href="https://poczta.onet.pl/"]')
        login_btn.click()

    def log_in_account(self, login=None, password=None):
        login_input = self.find_element(
            By.NAME, 'email'
        )
        login_input.send_keys(login)
        password_input = self.find_element(
            By.NAME, 'password'
        )
        password_input.send_keys(password)
        login_btn = self.find_element(
            By.CSS_SELECTOR, 'button[type="Submit"]'
        )
        login_btn.click()

    def create_new_message_and_send(self, address=None, topic_with_message=None):
        create_new_message_btn = self.find_element(
            By.CSS_SELECTOR, 'span[title="Napisz wiadomość"]'
        )
        create_new_message_btn.click()
        input_address = self.find_element(
            By.CSS_SELECTOR, 'input[type="email"]'
        )
        input_address.send_keys(address)
        input_title_with_message = self.find_element(
            By.CSS_SELECTOR, 'input[type="text"]'
        )
        input_title_with_message.send_keys(topic_with_message)
        active_btn_send_message = self.find_element(
            By.CSS_SELECTOR, 'button[title="Dodaj"]'
        )
        active_btn_send_message.click()
        send_btn = self.find_element(
            By.CSS_SELECTOR, 'button[title="Wyślij"]'
        )
        send_btn.click()
        confirm_btn = self.find_element(
            By.CSS_SELECTOR, 'button[title="Tak"]'
        )
        confirm_btn.click()
