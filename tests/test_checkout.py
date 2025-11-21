from pages.cart_page import CartPage
from utils.test_helpers import add_to_cart

def test_check_out(driver, login):

      add_to_cart(driver)
      cartpage = CartPage(driver)
      cartpage.click_add_to_cart()
      cartpage.click_view_cart()
      cartpage.click_proceed_to_checkout_button()
      cartpage.click_place_order()

