from selenium.webdriver.common.by import By
class LogoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.logout_button = (By.XPATH, '//a[@href="/logout"]')

    def click_logout(self):
        self.driver.find_element(*self.logout_button).click()



