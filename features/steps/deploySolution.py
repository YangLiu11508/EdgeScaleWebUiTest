from behave import *
from constant import Url
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@when('deploy solution')
def step_impl(context):
    context.driver.get(Url.BASE_URL + Url.SOLUTION)
    print("url = " + str(Url.BASE_URL + Url.SOLUTION))
    sleep(15)
    context.driver.find_element_by_link_text("Deploy").click()
    sleep(5)
    context.driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
    sleep(5)
    context.driver.find_element_by_xpath("(//input[@type='checkbox'])[2]").click()
    sleep(1)
    context.driver.find_element_by_xpath("//div[@id='inbox-toolbar-toggle-single']/div[2]/a/span").click()
    sleep(5)
    context.driver.find_element_by_xpath("//div[@id='inbox-toolbar-toggle-single']/div/a/span").click()

@then('deploy solution resultMessage {resultMessage}')
def step_impl(context, resultMessage):
    locator = (By.CSS_SELECTOR, '.el-notification.right>div>h2')
    isDeploySuccess = WebDriverWait(context.driver, 10, 0.5).until(
        EC.text_to_be_present_in_element(locator, resultMessage))
    assert isDeploySuccess == True