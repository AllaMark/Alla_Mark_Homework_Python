from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")

username = driver.find_element(By.CSS_SELECTOR, value = "[id='username']")
username.send_keys("tomsmith")

password = driver.find_element(By.CSS_SELECTOR, value = "[id='password']")
password.send_keys("SuperSecretPassword!")

wait = WebDriverWait(driver, 10)
button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "fa-sign-in")))
button.click()

success_message = driver.find_element(By.CSS_SELECTOR, value = "[id='flash']")
print(success_message.text)
driver.quit()

