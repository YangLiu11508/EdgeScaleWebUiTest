from behave import *
from constant import Url
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@when('deploy app')
def step_impl(context):
    context.driver.get(Url.BASE_URL + Url.APP)
    print("url = " + str(Url.BASE_URL + Url.APP))
    sleep(15)
    context.driver.find_element_by_xpath(
        "//div[@id='app']/div/div[2]/div/div[2]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/button[3]/span").click()
    sleep(3)
    context.driver.find_element_by_xpath(
        "//div[@id='app']/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div[4]/a/button/span").click()
    sleep(3)
    context.driver.find_element_by_xpath("//table[@id='DevicesDataTable']/tbody/tr/td/div/label/span/span").click()
    sleep(3)
    context.driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]").click()


@then('deploy app resultMessage {resultMessage}')
def step_impl(context, resultMessage):
    locator = (By.CSS_SELECTOR, '.el-notification.right>div>h2')
    isDeploySuccess = WebDriverWait(context.driver, 10, 0.5).until(
        EC.text_to_be_present_in_element(locator, resultMessage))
    assert isDeploySuccess == True

@when('delete task')
def step_impl(context):
    context.driver.get(Url.BASE_URL + Url.TASK)
    print("url = " + str(Url.BASE_URL + Url.TASK))
    sleep(15)
    context.driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/div[2]/div[2]/div/div/div/div/div[2]/div/div[3]/table/tbody/tr/td[6]/div/button/i").click()
    sleep(2)
    context.driver.find_element_by_xpath("(//button[@type='button'])[12]").click()


@then('delete task resultMessage {resultMessage}')
def step_impl(context, resultMessage):
    locator = (By.CSS_SELECTOR, '.el-notification.right>div>h2')
    isDeleteSuccess = WebDriverWait(context.driver, 10, 0.5).until(
        EC.text_to_be_present_in_element(locator, resultMessage))
    assert isDeleteSuccess == True