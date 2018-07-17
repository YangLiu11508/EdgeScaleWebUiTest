from behave import *
from constant import Url
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@when('add tag to solution with tag {tag}')
def step_impl(context, tag):
    context.driver.get(Url.BASE_URL + Url.SOLUTION)
    print("url = " + str(Url.BASE_URL + Url.SOLUTION))
    sleep(15)
    context.driver.find_element_by_xpath(
        "//div[@id='app']/div/div[2]/div/div[2]/div[2]/div/div/div/div/div[2]/div/div[2]/div/div/div/div/div/div[3]/div/div/div/button/span").click()
    context.driver.find_element_by_xpath("(//input[@type='text'])[5]").clear()
    context.driver.find_element_by_xpath("(//input[@type='text'])[5]").send_keys(tag)
    sleep(1)
    context.driver.find_element_by_xpath("(//input[@type='text'])[5]").send_keys(Keys.ENTER)

@then('add tag to solution resultMessage {resultMessage}')
def step_impl(context, resultMessage):
    locator = (By.CSS_SELECTOR, '.el-notification.right>div>h2')
    isAddSuccess = WebDriverWait(context.driver, 10, 0.5).until(
        EC.text_to_be_present_in_element(locator, resultMessage))
    assert isAddSuccess == True

@when('delete tag from solution')
def step_impl(context):
    context.driver.get(Url.BASE_URL + Url.SOLUTION)
    print("url = " + str(Url.BASE_URL + Url.SOLUTION))
    sleep(15)
    context.driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/div[2]/div[2]/div/div/div/div/div[2]/div/div[2]/div/div/div/div/div/div[3]/div/div[2]/span/span/span/i").click()


@then('delete tag from solution resultMessage {resultMessage}')
def step_impl(context, resultMessage):
    locator = (By.CSS_SELECTOR, '.el-notification.right>div>h2')
    isDeleteSuccess = WebDriverWait(context.driver, 10, 0.5).until(
        EC.text_to_be_present_in_element(locator, resultMessage))
    assert isDeleteSuccess == True