import pytest
from selenium import webdriver
import time
import pytest

driver = None
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser")
    if browser_name == "chrome":
        browser_options = webdriver.ChromeOptions()
        browser_options.add_argument("--ignre-certificate-errors")
        browser_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=browser_options)
    elif browser_name == "firefox":
        browser_options = webdriver.FirefoxOptions()
        browser_options.add_argument("--ignre-certificate-errors")
        browser_options.add_argument("--start-maximized")
        driver = webdriver.Firefox(options=browser_options)
    elif browser_name == "edge":
        browser_options = webdriver.EdgeOptions()
        browser_options.add_argument("--ignre-certificate-errors")
        browser_options.add_argument("--start-maximized")
        driver = webdriver.Edge(options=browser_options)
    elif browser_name == "safari":
        browser_options = webdriver.SafariOptions()
        browser_options.add_argument("--ignre-certificate-errors")
        browser_options.add_argument("--start-maximized")
        driver = webdriver.Safari(options=browser_options)
    else:
        browser_options = webdriver.ChromeOptions()
        browser_options.add_argument("--ignre-certificate-errors")
        browser_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=browser_options)
    driver.implicitly_wait(10)  # global timeout max 5 seconds 2 or 3, timeout done
    driver.get('https://rahulshettyacademy.com/angularpractice/')
    print(driver.current_url)
    print(driver.title)
    request.cls.driver = driver
    yield
    driver.close()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
