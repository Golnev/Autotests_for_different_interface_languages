from selenium.webdriver.common.by import By
import time


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_user_see_button_add_to_basket(browser):
    browser.get(link)
    time.sleep(13)
    button_add_to_basket = browser.find_elements(By.CSS_SELECTOR, '.btn-add-to-basket')
    assert len(button_add_to_basket) == 1, 'No button "add to basket"' if len(button_add_to_basket) == 0 else\
        'There more then 1 button with "btn-add-to-basket" class.'
