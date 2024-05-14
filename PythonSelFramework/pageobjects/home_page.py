from selenium.webdriver.common.by import By

from pageobjects.checkout_page import CheckoutPage


class HomePage:
    shop = (By.XPATH, "//a[text()='Shop']")
    nameBox = (By.CSS_SELECTOR, "div[class='form-group'] input[name='name']")
    emailBox = (By.XPATH, "//div[@class='form-group']/input[@name='email']")
    passBox = (By.ID, "exampleInputPassword1")
    cb1 = (By.ID, "exampleCheck1")
    maleBoxControl = (By.XPATH, "//div[@class='form-group']/select[@id='exampleFormControlSelect1']")
    radioStatusBtn = (By.XPATH, "//div[@class='form-check form-check-inline']/input[@id='inlineRadio2']")
    birthdayBox = (By.XPATH, "//div[@class='form-group']/input[@name='bday']")
    submitBtn = (By.XPATH, "//input[@class='btn btn-success']")
    successMsg = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")
    # shop = (By.XPATH, "//a[text()='Shop']")
    # shop = (By.XPATH, "//a[text()='Shop']")
    # shop = (By.XPATH, "//a[text()='Shop']")
    # shop = (By.XPATH, "//a[text()='Shop']")
    # shop = (By.XPATH, "//a[text()='Shop']")

    def __init__(self, driver):
        self.driver = driver

    def shop_items(self):
        self.driver.find_element(*HomePage.shop).click()  # * deserializes a tuple
        # self.driver.find_element(By.XPATH, "//a[text()='Shop']")
        checkoutpage = CheckoutPage(self.driver)
        return checkoutpage

    def enter_name(self):
        return self.driver.find_element(*HomePage.nameBox)

    def enter_email(self):
        return self.driver.find_element(*HomePage.emailBox)

    def enter_password(self):
        return self.driver.find_element(*HomePage.passBox)

    def get_checkbox(self):
        return self.driver.find_element(*HomePage.cb1)

    def get_maleBoxControl(self):
        return self.driver.find_element(*HomePage.maleBoxControl)

    def get_radioStatusBtn(self):
        return self.driver.find_element(*HomePage.radioStatusBtn)

    def get_birthdayBox(self):
        return self.driver.find_element(*HomePage.birthdayBox)

    def get_submitBtn(self):
        return self.driver.find_element(*HomePage.submitBtn)

    def get_successMsg(self):
        return self.driver.find_element(*HomePage.successMsg)