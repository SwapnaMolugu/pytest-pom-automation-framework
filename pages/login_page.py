from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.signup_login_button =  (By.XPATH, '//a[@href="/login"]')
        self.email_input = (By.NAME, 'email')
        self.password_input = (By.CSS_SELECTOR, 'input[data-qa="login-password"]')
        self.login_button = (By.CSS_SELECTOR, 'button[data-qa="login-button"]')

    def click_signup_login(self):
        self.driver.find_element(*self.signup_login_button).click()

    def enter_email(self, username):
        self.driver.find_element(*self.email_input).clear()
        self.driver.find_element(*self.email_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).clear()
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def login(self, username, password):
        self.click_signup_login()
        self.enter_email(username)
        self.enter_password(password)
        self.click_login()