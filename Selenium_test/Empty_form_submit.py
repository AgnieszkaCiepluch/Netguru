# coding=utf-8
import driver as driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.remote.webelement import WebElement
import re
from selenium.webdriver.support.color import Color


driver = webdriver.Chrome(executable_path=r"C:\Users\Dell\PycharmProjects\seleniumwebd\Selenium\drivers\chromedriver")

driver.get("https://www.tui.pl/")

print(driver.title)
print(driver.current_url)

driver.find_element(By.CLASS_NAME, "my-tui").click()
time.sleep(2)

driver.switch_to.window(driver.window_handles[1])

email = driver.find_element(By.ID, "email")
password = driver.find_element(By.ID, "pass")

email.clear()
password.clear()

rgb = email.value_of_css_property('background-color')
hex = Color.from_string(rgb).hex
print("E-mail input color is: ", hex)

rgb = password.value_of_css_property('background-color')
hex = Color.from_string(rgb).hex
print("Password input color is: ", hex)

driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
time.sleep(2)

form_message = driver.find_element_by_css_selector("form-message")
print("Alerts are displayed: ", form_message.is_displayed())

print ("\n Email alert and input color:")

emailAlert = driver.find_element(By.CSS_SELECTOR, 'form-message[content = "Wpisz poprawny adres e-mail."]')
print("Email alert is displayed: ", emailAlert.is_displayed())
# driver.getCssValue(email, 'background-color')
rgb = email.value_of_css_property('background-color')
hex = Color.from_string(rgb).hex
print("Color of email input changed to: ", hex)


print ("\n Password alert and input color:")

passAlert = driver.find_element(By.CSS_SELECTOR, 'form-message[content = "Wpisz hasło."]')
print("Password alert is displayed: ", passAlert.is_displayed())
rgb = password.value_of_css_property('background-color')
hex = Color.from_string(rgb).hex
print("Color of password input changed to: ", hex)

# driver.close()
driver.quit()