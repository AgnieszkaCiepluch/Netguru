# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import unittest
from selenium.webdriver.support.color import Color


class SignIn(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path=r"C:\Users\Dell\PycharmProjects\seleniumwebd\Selenium\drivers\chromedriver")

        self.driver.get("https://www.tui.pl/")

        print(self.driver.title)
        print(self.driver.current_url)

    def test_empty_form_submitted(self):
        self.driver.find_element(By.CLASS_NAME, "my-tui").click()
        time.sleep(2)

        self.driver.switch_to.window(self.driver.window_handles[1])

        email = self.driver.find_element(By.ID, "email")
        password = self.driver.find_element(By.ID, "pass")
        email.clear()
        password.clear()
        rgb = email.value_of_css_property('background-color')
        hex = Color.from_string(rgb).hex
        print("E-mail input color is: ", hex)

        rgb = password.value_of_css_property('background-color')
        hex = Color.from_string(rgb).hex
        print("Password input color is: ", hex)

        self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        time.sleep(2)

        form_message = self.driver.find_element_by_css_selector("form-message")
        print("Alerts are displayed: ", form_message.is_displayed())

        print ("\n Email alert and input color:")

        emailAlert = self.driver.find_element(By.CSS_SELECTOR, 'form-message[content = "Wpisz poprawny adres e-mail."]')
        print("Email alert is displayed: ", emailAlert.is_displayed())
        # driver.getCssValue(email, 'background-color')
        rgb = email.value_of_css_property('background-color')
        hex = Color.from_string(rgb).hex
        print("Color of email input changed to: ", hex)

        print ("\n Password alert and input color:")

        passAlert = self.driver.find_element(By.CSS_SELECTOR, 'form-message[content = "Wpisz hasło."]')
        print("Password alert is displayed: ", passAlert.is_displayed())
        rgb = password.value_of_css_property('background-color')
        hex = Color.from_string(rgb).hex
        print("Color of password input changed to: ", hex)

    def test_empty_password_submitted(self):
        self.driver.find_element(By.CLASS_NAME, "my-tui").click()
        time.sleep(2)
        self.driver.find_element(By.CLASS_NAME, "my-tui").click()
        time.sleep(2)

        self.driver.switch_to.window(self.driver.window_handles[1])

        email = self.driver.find_element(By.ID, "email")
        password = self.driver.find_element(By.ID, "pass")
        email.clear()
        email.send_keys("agnieszka@gmail.com")

        password.clear()

        rgb = email.value_of_css_property('background-color')
        hex = Color.from_string(rgb).hex
        print(hex)

        rgb = password.value_of_css_property('background-color')
        hex = Color.from_string(rgb).hex
        print(hex)

        self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        time.sleep(2)

        print ("\n Password alert and input color:")
        passAlert = self.driver.find_element(By.CSS_SELECTOR, 'form-message[content = "Wpisz hasło."]')
        print("Password alert is displayed: ", passAlert.is_displayed())
        rgb = password.value_of_css_property('background-color')
        hex = Color.from_string(rgb).hex
        print("Color of input changed to: ", hex)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test completed!")
