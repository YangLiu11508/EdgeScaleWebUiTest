from behave import *
from constant import Url
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@when('deploy multiple app')
def step_impl(context):
    context.driver.get(Url.BASE_URL + Url.APP)
    print("url = " + str(Url.BASE_URL + Url.APP))
    sleep(15)
    context.driver.find_element_by_xpath(
        "//div[@id='app']/div/div[2]/div/div[2]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/button[2]/i").click()
    sleep(5)
    context.driver.find_element_by_xpath("(//input[@type='checkbox'])[2]").click()
    sleep(1)
    context.driver.find_element_by_xpath("(//input[@type='checkbox'])[3]").click()
    sleep(1)
    context.driver.find_element_by_xpath("//div[@id='inbox-toolbar-toggle-single']/div[2]/a/span").click()
    sleep(5)
    context.driver.find_element_by_xpath("(//input[@type='checkbox'])[2]").click()
    sleep(5)
    context.driver.find_element_by_xpath("(//input[@type='checkbox'])[3]").click()
    sleep(5)
    context.driver.find_element_by_xpath("//div[@id='inbox-toolbar-toggle-single']/div[2]/a/span").click()
    sleep(5)
    context.driver.find_element_by_xpath(
        "//div[@id='app']/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/div/a/span").click()
    sleep(5)
    context.driver.find_element_by_xpath("//div[@id='inbox-toolbar-toggle-single']/div/a/span").click()


@then('deploy multiple app resultMessage {resultMessage}')
def step_impl(context, resultMessage):
    locator = (By.CSS_SELECTOR, '.el-notification.right>div>h2')
    isDeploySuccess = WebDriverWait(context.driver, 10, 0.5).until(
        EC.text_to_be_present_in_element(locator, resultMessage))
    assert isDeploySuccess == True