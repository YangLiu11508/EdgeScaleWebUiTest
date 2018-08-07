from behave import *
from constant import Url
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@when('setting limit with limitType {limitType}, limit {limit}')
def step_impl(context,limitType,limit):
    context.driver.get(Url.BASE_URL + Url.USER)
    print("url = " + str(Url.BASE_URL + Url.USER))
    sleep(15)
    context.driver.find_element_by_xpath(
        "//div[@id='app']/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div/div[3]/table/tbody/tr/td[5]/div/button/i").click()
    sleep(1)
    context.driver.find_element_by_xpath("(//input[@type='text'])[4]").click()
    sleep(1)
    context.driver.find_element_by_xpath("//div[4]/div/div/ul/li/span").click()
    sleep(1)
    context.driver.find_element_by_xpath("//input[@type='number']").click()
    context.driver.find_element_by_xpath("//input[@type='number']").clear()
    context.driver.find_element_by_xpath("//input[@type='number']").send_keys(limit)
    sleep(1)
    context.driver.find_element_by_xpath("(//button[@type='button'])[19]").click()


@then('setting limit resultMessage {resultMessage}')
def step_impl(context, resultMessage):
    locator = (By.CSS_SELECTOR, 'div.el-message.el-message--success>p')
    isDeploySuccess = WebDriverWait(context.driver, 10, 0.5).until(
        EC.text_to_be_present_in_element(locator, resultMessage))
    assert isDeploySuccess == True