link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
def test_check_button(browser):
    browser.get(link)
    browser.implicitly_wait(5)
    button = browser.find_element_by_css_selector(".btn.btn-lg.btn-primary.btn-add-to-basket")