# coding=utf-8
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
email.send_keys("agnieszka@gmail.com")

password.clear()

rgb = email.value_of_css_property('background-color')
hex = Color.from_string(rgb).hex
print(hex)

rgb = password.value_of_css_property('background-color')
hex = Color.from_string(rgb).hex
print(hex)

driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
time.sleep(2)

print ("\n Password alert and input color:")
passAlert = driver.find_element(By.CSS_SELECTOR, 'form-message[content = "Wpisz hasło."]')
print("Password alert is displayed: ", passAlert.is_displayed())
rgb = password.value_of_css_property('background-color')
hex = Color.from_string(rgb).hex
print("Color of input changed to: ", hex)


driver.quit()
