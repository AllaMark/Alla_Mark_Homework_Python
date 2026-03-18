from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/dynamicid")

wait = WebDriverWait(driver, 10)
button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "btn-primary")))
button.click()

sleep(3)