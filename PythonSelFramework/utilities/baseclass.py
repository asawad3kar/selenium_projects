import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:
    def verifyLinkTextPresence(self, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def selectOptionByVisibleText(self, locator, text):
        select_obj = Select(locator)
        select_obj.select_by_visible_text(text)

    def scroll(self, x_disp, y_disp):
        script_text = f"window.scrollTo({x_disp}, {y_disp});"
        self.driver.execute_script(script_text)

    def getLogger(self):
        loggername = inspect.stack()[1][3]
        # logger = logging.getLogger(__name__)  # filename name is generated by default it prints root
        logger = logging.getLogger(loggername)  # filename name is generated by default it prints root

        filehandler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)  # takes filehandler object
        logger.setLevel(logging.DEBUG)
        # logger.debug("A debug statemeent is executed")
        # logger.info("Information statement")
        # logger.warning("Something in warning mode")
        # logger.error("MAJOR ERROR")
        # logger.critical("Critical issue")
        return logger