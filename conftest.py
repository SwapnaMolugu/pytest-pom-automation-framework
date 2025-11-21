import pytest
import logging
from selenium import webdriver #WebDriver module to control the browser (Chrome, Firefox, etc.).
from selenium.webdriver.chrome.service import Service #  Service, which is needed to launch Chrome with a specified ChromeDriver executable
from webdriver_manager.chrome import ChromeDriverManager # which automatically downloads and manages the correct ChromeDriver version for you
from pages.product_page import ProductPage

from pages.login_page import LoginPage
from utils.data_reader.config_loader import load_config


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) # Launches a new Chrome browser, managed through Selenium.
    driver.maximize_window()
    yield driver # Pauses here and provides the driver to your test function.While the test runs, the browser remains available.
    driver.quit()

@pytest.fixture(scope='function')
def login(driver):
    # Load credentials from config
    config = load_config("credentials")
    username = config["login"]["username"] # in config you can login and then username & password
    password = config["login"]["password"]

    # Navigate to the login page
    driver.get("https://automationexercise.com/")

    # Perform login
    login_page = LoginPage(driver)
    login_page.login(username, password)

#loggin code

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("mylog.log"),
              logging.StreamHandler()]
)
logging.info("Test started")
logging.error("something went wrong")

#saves the screenshot if test fail
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            file_name = f"screenshots/{item.name}_failure.png"
            driver.save_screenshot(file_name)
            print(f"\n[INFO] Screenshot for {item.name} saved to {file_name}")


