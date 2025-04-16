from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5500/index.html")  # adjust if using a different port/path

time.sleep(1)
driver.find_element(By.ID, "num1").send_keys("3")
driver.find_element(By.ID, "num2").send_keys("4")
driver.find_element(By.TAG_NAME, "button").click()
time.sleep(1)

result = driver.find_element(By.ID, "res").text
print("✅ Test passed" if result == "7" else f"❌ Test failed. Found: {result}")

driver.quit()
