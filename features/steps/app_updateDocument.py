from behave import *
from constant import Url
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@when('update app document with content {content}')
def step_impl(context,content):
    context.driver.get(Url.BASE_URL + Url.APP)
    print("url = " + str(Url.BASE_URL + Url.APP))
    sleep(15)
    context.driver.find_element_by_xpath(
        "//div[@id='app']/div/div[2]/div/div[2]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/button[3]/span").click()
    sleep(5)
    context.driver.find_element_by_xpath(
        "//div[@id='app']/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div[5]/a/button/span").click()
    sleep(5)
    context.driver.find_element_by_xpath(
        "//div[@id='app']/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div/p").click()
    sleep(1)
    context.driver.find_element_by_xpath(
        "//div[@id='app']/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div/p").clear()
    element=context.driver.find_element_by_xpath(
        "//div[@id='app']/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div")
    print("element============"+element.get_attribute("class"))
    element.send_keys("1234")

    sleep(3)
    context.driver.find_element_by_xpath("(//button[@type='button'])[21]").click()


@then('update app document resultMessage {resultMessage}')
def step_impl(context, resultMessage):
    locator = (By.CSS_SELECTOR, 'div.el-message.el-message--success>p')
    isUpdateSuccess = WebDriverWait(context.driver, 10, 0.5).until(
        EC.text_to_be_present_in_element(locator, resultMessage))
    assert isUpdateSuccess == True