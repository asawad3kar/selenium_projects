from selenium.webdriver.common.by import By

from pageobjects.confirm_page import ConfirmPage


class CheckoutPage:
    cardTitle = (By.XPATH, "//div[@class='card h-100']")
    cardFooter = (By.XPATH, "//div[@class='card h-100']/div/h4/a")
    cardButton = (By.XPATH, "//div[@class='card h-100']/div/button")
    btnPrimary = (By.CSS_SELECTOR, ".btn-primary")
    btnSuccess = (By.XPATH, "//button[@class='btn btn-success']")

    def __init__(self, driver):
        self.driver = driver

    def getCardTitle(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_element(*CheckoutPage.cardFooter)

    def getCardButton(self):
        return self.driver.find_element(*CheckoutPage.cardButton)

    def getPrimaryButton(self):
        return self.driver.find_element(*CheckoutPage.btnPrimary)

    def getSuccessButton(self):
        self.driver.find_element(*CheckoutPage.btnSuccess).click()
        confirmpage = ConfirmPage(self.driver)
        return confirmpage