#DAY 04
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.ID, "checkBoxOption1").click()
driver.find_element(By.CLASS_NAME, "radioButton").click()
driver.find_element(By.NAME, "radioButton").click()
driver.find_element(By.LINK_TEXT, "🎯 I’ll help you prepare for your next QA job — Explore the QA Career Accelerator.").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "🎯 I’ll help you prepare for your").click()

