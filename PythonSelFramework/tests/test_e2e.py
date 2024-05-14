from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from pageobjects.checkout_page import CheckoutPage
from pageobjects.confirm_page import ConfirmPage
from utilities.baseclass import BaseClass
from pageobjects.home_page import HomePage


class TestOne(BaseClass):

    def test_e2e(self):
        logger = self.getLogger()
        homepage = HomePage(self.driver)
        checkoutpage = homepage.shop_items() #TriggerPoint

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight-50);")

        products = checkoutpage.getCardTitle()
        logger.info(f"No of items : {len(products)}")
        logger.info("Getting all the items")
        for prod in products:
            # product_name = checkoutpage.getCardFooter().text
            # logger.info(f"{product_name}")
            if "Blackberry" in prod.text:
            # if product_name == 'Blackberry':
                logger.info("Selecting Blackberry")
                checkoutpage.getCardButton().click()
        self.driver.execute_script("window.scrollTo(0, 50);")
        checkoutpage.getPrimaryButton().click()
        confirmpage = checkoutpage.getSuccessButton() #TriggerPoint
        logger.info("Entering country name")
        confirmpage.getCountryID().send_keys("ind")
        # wait = WebDriverWait(self.driver, 10)
        # wait.until(confirmpage.presenceOfIndiaText())
        self.verifyLinkTextPresence("India")
        confirmpage.getIndia().click()
        confirmpage.getcheckBoxPrim().click()
        confirmpage.getSubmitButton().click()
        message = confirmpage.getMessageText().text
        logger.info(f"Text received from application is {message}")
        assert "Success" in str(message)
