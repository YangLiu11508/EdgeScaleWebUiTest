from behave import *
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@when('bind tag with tag {tag}')
def step_impl(context, tag):
    sleep(5)
    context.driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/div/div/div/div/ul/li[5]/a/i").click()
    sleep(2)
    context.driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/div/div/div/div/ul/li[5]/a/i").click()
    sleep(2)
    context.driver.find_element_by_link_text("My Devices").click()
    sleep(5)
    context.driver.find_element_by_xpath("(//input[@type='checkbox'])[2]").click()
    context.driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/a/span").click()
    context.driver.find_element_by_xpath("(//input[@type='text'])[5]").click()
    sleep(2)
    context.driver.find_element_by_xpath("(//input[@type='text'])[5]").clear()
    context.driver.find_element_by_xpath("(//input[@type='text'])[5]").send_keys(tag)
    sleep(5)
    element = context.driver.find_element_by_xpath("//ul[@class='el-scrollbar__view el-select-dropdown__list']")
    element.find_element_by_xpath("//li/span[text()= '" + tag + "']").click()
    sleep(2)
    context.driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/div[2]/div[2]/div/div/div/div[4]/div/div[3]/div/button/span").click()


@then('bind tag resultMessage {resultMessage}')
def step_impl(context, resultMessage):
    locator = (By.CSS_SELECTOR, '.el-notification.right>div>h2')
    isAddSuccess = WebDriverWait(context.driver, 10, 0.5).until(
        EC.text_to_be_present_in_element(locator, resultMessage))
    assert isAddSuccess == True


@when('delete bind tag')
def step_impl(context):
    sleep(5)
    context.driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/div/div/div/div/ul/li[5]/a/i").click()
    sleep(1)
    context.driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/div/div/div/div/ul/li[5]/a/i").click()
    sleep(1)
    context.driver.find_element_by_link_text("My Devices").click()
    sleep(5)
    context.driver.find_element_by_xpath(
    "//div[@id='app']/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/div[4]/div/span/span/span/span/i").click()


@then('delete bind tag resultMessage {resultMessage}')
def step_impl(context, resultMessage):
    locator = (By.CSS_SELECTOR, '.el-notification.right>div>h2')
    isDeleteSuccess = WebDriverWait(context.driver, 10, 0.5).until(
        EC.text_to_be_present_in_element(locator, resultMessage))
    assert isDeleteSuccess == True
