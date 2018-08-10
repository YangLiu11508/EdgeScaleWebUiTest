from behave import *
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from constant import Url

@when('inactive device')
def step_impl(context):
    sleep(5)
    context.driver.get(Url.BASE_URL + Url.DEVICE)
    print("device list url = " + str(Url.BASE_URL + Url.DEVICE))
    sleep(10)
    context.driver.find_element_by_xpath(
    "//div[@id='app']/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/ul/li/button/span").click()
    sleep(2)
    context.driver.find_element_by_xpath("//div[3]/button[2]/span").click()


@then('inactive resultMessage {resultMessage}')
def step_impl(context, resultMessage):
    locator = (By.CSS_SELECTOR, 'div.el-message.el-message--success>p')
    isInactiveSuccess = WebDriverWait(context.driver, 10, 0.5).until(
        EC.text_to_be_present_in_element(locator, resultMessage))
    assert isInactiveSuccess == True


@when('active device')
def step_impl(context):
    sleep(5)
    context.driver.get(Url.BASE_URL + Url.DEVICE)
    print("device list url = " + str(Url.BASE_URL + Url.DEVICE))
    sleep(10)
    context.driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/ul/li/button/span").click()
    sleep(1)
    context.driver.find_element_by_xpath("//div[3]/button[2]/span").click()

@then('active resultMessage {resultMessage}')
def step_impl(context, resultMessage):
    locator = (By.CSS_SELECTOR, 'div.el-message.el-message--success>p')
    isDeleteSuccess = WebDriverWait(context.driver, 10, 0.5).until(
        EC.text_to_be_present_in_element(locator, resultMessage))
    assert isDeleteSuccess == True
