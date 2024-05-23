import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options=Options()
options.add_experimental_option("detach",True)
driver= webdriver.Chrome(options=options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.find_element(By.ID,"checkBoxOption1").click()
driver.find_element(By.NAME,"checkBoxOption2").click()
driver.find_element(By.CLASS_NAME,"radioButton").click()
time.sleep(2)