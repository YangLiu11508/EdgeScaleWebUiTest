from behave import *
from constant import Url
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@when('edit solution with link {link}, permission {permission}')
def step_impl(context,link,permission):
    context.driver.get(Url.BASE_URL + Url.SOLUTION)
    print("url = " + str(Url.BASE_URL + Url.SOLUTION))
    sleep(15)
    context.driver.find_element_by_link_text("Edit").click()
    sleep(5)
    context.driver.find_element_by_xpath("//input[@type='text']").click()
    context.driver.find_element_by_xpath("//input[@type='text']").clear()
    context.driver.find_element_by_xpath("//input[@type='text']").send_keys(link)
    sleep(2)
    context.driver.find_element_by_xpath(
        "//form[@id='editSolutionFormSubmit']/fieldset/div[2]/div/div/label[2]/span/span").click()
    sleep(1)
    context.driver.find_element_by_xpath("//form[@id='editSolutionFormSubmit']/fieldset/div[3]/div/div/button[2]/span/i").click()


@then('edit solution resultMessage {resultMessage}')
def step_impl(context, resultMessage):
    locator = (By.CSS_SELECTOR, '.el-notification.right>div>h2')
    isEditSuccess = WebDriverWait(context.driver, 10, 0.5).until(
        EC.text_to_be_present_in_element(locator, resultMessage))
    assert isEditSuccess == True