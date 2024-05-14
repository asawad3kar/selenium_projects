from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class ConfirmPage():
    countryID = (By.ID, "country")
    linkTextIndia = (By.LINK_TEXT, "India")
    checkBoxPrim = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    submitButton = (By.XPATH, "//input[@type='submit']")
    messageText = (By.CLASS_NAME, "alert-success")

    def __init__(self, driver):
        self.driver = driver

    def getCountryID(self):
        return self.driver.find_element(*ConfirmPage.countryID)


    def getIndia(self):
        return self.driver.find_element(*ConfirmPage.linkTextIndia)

    def getcheckBoxPrim(self):
        return self.driver.find_element(*ConfirmPage.checkBoxPrim)

    def getSubmitButton(self):
        return self.driver.find_element(*ConfirmPage.submitButton)

    def getMessageText(self):
        return self.driver.find_element(*ConfirmPage.messageText)