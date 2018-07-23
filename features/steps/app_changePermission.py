from behave import *
from constant import Url
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@when('change permission')
def step_impl(context):
    context.driver.get(Url.BASE_URL + Url.APP)
    print("url = " + str(Url.BASE_URL + Url.APP))
    sleep(10)
    context.driver.find_element_by_xpath(
        "//div[@id='app']/div/div[2]/div/div[2]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/button[3]/i").click()
    sleep(2)
    context.driver.find_element_by_xpath(
        "//div[@id='app']/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/a/h6").click()
    sleep(5)
    context.driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div/button/i").click()
    sleep(5)
    context.driver.find_element_by_xpath(
        "//div[@id='app']/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div/label[2]/span[2]").click()
    sleep(2)
    context.driver.find_element_by_xpath("(//button[@type='button'])[3]").click()

@then('change permission resultMessage {resultMessage}')
def step_impl(context, resultMessage):
    locator = (By.CSS_SELECTOR, '.el-notification.right>div>h2')
    isChangeSuccess = WebDriverWait(context.driver, 10, 0.5).until(
        EC.text_to_be_present_in_element(locator, resultMessage))
    assert isChangeSuccess == True