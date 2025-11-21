from pages.product_page import ProductPage
from pages.cart_page import CartPage

def add_to_cart(driver):
        product_page = ProductPage(driver)
        product_page.click_product_button()
        product_page.click_women_category_button()
        product_page.click_dress_category_button()
        product_page.click_on_dress_tile()

def check_out(driver, login):
      add_to_cart(driver)
      cartpage = CartPage(driver)
      cartpage.click_add_to_cart()
      cartpage.click_view_cart()
      cartpage.click_proceed_to_checkout_button()
      cartpage.click_place_order()
