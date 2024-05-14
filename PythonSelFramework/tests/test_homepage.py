import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageobjects.home_page import HomePage
from utilities.baseclass import BaseClass


class TestHomePage(BaseClass):
    def test_formSubmission(self, getData):
        logger = self.getLogger()
        homepage = HomePage(self.driver)
        logger.info(f"Running tests for {getData['name']}")
        homepage.enter_name().send_keys(getData["name"])
        homepage.enter_email().send_keys(getData["email"])
        homepage.enter_password().send_keys(getData["password"])
        homepage.get_checkbox().click()
        self.selectOptionByVisibleText(homepage.get_maleBoxControl(), getData["gender"])
        self.scroll("0", "document.body.scrollHeight-50")
        homepage.get_radioStatusBtn().click()
        homepage.get_birthdayBox().send_keys(getData["dob"])
        homepage.get_submitBtn().click()
        message_text = homepage.get_successMsg().text
        assert "Success!" in message_text
        self.driver.refresh()

    @pytest.fixture(
        params=HomePageData.test_HomePageData)
    def getData(self, request):
        return request.param
