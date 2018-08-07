from behave import *
from constant import Url
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@when('create vendor with vendor {vendor}')
def step_impl(context,vendor):
    # 使用URL的方式会出现不显示Create Model 按钮
    # context.driver.get(Url.BASE_URL + Url.MODEL)
    # print("url = " + str(Url.BASE_URL + Url.MODEL))
    sleep(10)
    context.driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/div/div/div/div/ul/li[9]/a/i").click()
    sleep(3)
    context.driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/div/div/div/div/ul/li[9]/a/span").click()
    sleep(1)
    context.driver.find_element_by_link_text("Vendor").click()
    sleep(5)
    context.driver.find_element_by_xpath(
        "//div[@id='app']/div/div[2]/div/div[2]/div[2]/div/div/div/div/div/button/span").click()
    sleep(5)
    # 输入vendor
    context.driver.find_element_by_xpath("//input[@type='text']").click()
    context.driver.find_element_by_xpath("//input[@type='text']").clear()
    context.driver.find_element_by_xpath("//input[@type='text']").send_keys(vendor)
    sleep(1)
    # 点击提交
    context.driver.find_element_by_xpath(
        "//div[@id='app']/div/div[2]/div/div[2]/div[2]/div/div/div/div/form/div[2]/div/button[2]/span").click()


@then('create vendor resultMessage {resultMessage}')
def step_impl(context, resultMessage):
    locator = (By.CSS_SELECTOR, '.el-notification.right>div>h2')
    isCreateSuccess = WebDriverWait(context.driver, 10, 0.5).until(
        EC.text_to_be_present_in_element(locator, resultMessage))
    assert isCreateSuccess == True

@when('delete vendor')
def step_impl(context):
    # 使用URL的方式会出现不显示Create Model 按钮
    # context.driver.get(Url.BASE_URL + Url.VENDOR)
    # print("url = " + str(Url.BASE_URL + Url.VENDOR))
    sleep(10)
    context.driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/div/div/div/div/ul/li[9]/a/i").click()
    sleep(3)
    context.driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/div/div/div/div/ul/li[9]/a/span").click()
    sleep(1)
    context.driver.find_element_by_link_text("Vendor").click()
    sleep(10)
    context.driver.find_element_by_xpath(
        "(.//*[normalize-space(text()) and normalize-space(.)='vendortest'])[1]/following::i[2]").click()
    sleep(1)
    context.driver.find_element_by_xpath(
        "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[2]/following::button[1]").click()



@then('delete vendor resultMessage {resultMessage}')
def step_impl(context, resultMessage):
    locator = (By.CSS_SELECTOR, '.el-notification.right>div>h2')
    isCreateSuccess = WebDriverWait(context.driver, 10, 0.5).until(
        EC.text_to_be_present_in_element(locator, resultMessage))
    assert isCreateSuccess == True

