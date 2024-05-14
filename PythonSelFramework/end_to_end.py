from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("headless")
chrome_options.add_argument("--ignre-certificate-errors")
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(10)  # global timeout max 5 seconds 2 or 3, timeout done
driver.get('https://rahulshettyacademy.com/angularpractice/')
# driver.maximize_window()
print(driver.current_url)
print(driver.title)
driver.find_element(By.XPATH, "//a[text()='Shop']").click()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight-50);")
products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
print(len(products))
for prod in products:
    product_name = prod.find_element(By.XPATH, "div/h4/a").text
    if product_name == 'Blackberry':
        prod.find_element(By.XPATH, "div/button").click()
driver.execute_script("window.scrollTo(0, 50);")
# driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']").click() #when * partial is enough
driver.find_element(By.CSS_SELECTOR,".btn-primary").click() #when * partial is enough
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
driver.find_element(By.ID, "country").send_keys("ind")
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()
# driver.find_element(By.ID, "checkbox2").click() #todo THIS DOESN'T WORK WHY??
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
assert "Success" in str(message)
driver.close()
# time.sleep(5)