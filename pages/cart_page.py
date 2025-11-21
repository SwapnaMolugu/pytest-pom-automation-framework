from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver

        self.add_to_cart_button = (By.XPATH, "//button[@class='btn btn-default cart']")
        # self.add_to_cart_button = (By.XPATH, "//a[@class='btn btn-default add-to-cart' and @data-product-id='3']")
        self.view_cart_button = (By.XPATH, "//a[.//u[text()='View Cart']]")
        self.proceed_to_checkout_button = (By.XPATH, '//a[@class="btn btn-default check_out" and text()="Proceed To Checkout"]')
        self.place_order_button = (By.XPATH,
                                   '//a[@href="/payment" and @class="btn btn-default check_out" and text()="Place Order"]')


    def click_add_to_cart(self):
        self.driver.find_element(*self.add_to_cart_button).click()

    # def click_view_cart(self):
    #     self.driver.find_element(*self.view_cart_button).click()
    def click_view_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.view_cart_button)
        ).click()


    def click_proceed_to_checkout_button(self):
        self.driver.find_element(*self.proceed_to_checkout_button).click()

    def click_place_order(self):
        self.driver.find_element(*self.place_order_button).click()