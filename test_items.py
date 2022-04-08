import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element_by_css_selector(".btn-add-to-basket").click()
    browser.find_element_by_css_selector("div.alertinner  a:nth-child(1)").click()
    addbasket = browser.find_element_by_css_selector('div.col-sm-4 h3 a').text
    assert addbasket == "Coders at Work", "book dont add"
