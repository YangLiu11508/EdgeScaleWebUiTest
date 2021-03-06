from behave import *
from constant import Url
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@when('create mirror with Mirror {Mirror}, Description {Description}')
def step_impl(context,Mirror,Description):
    # 使用URL的方式会出现不显示Create Model 按钮
    # context.driver.get(Url.BASE_URL + Url.MODEL)
    # print("url = " + str(Url.BASE_URL + Url.MODEL))
    sleep(10)
    context.driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/div/div/div/div/ul/li[9]/a/i").click()
    sleep(3)
    context.driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/div/div/div/div/ul/li[9]/a/span").click()
    sleep(1)
    context.driver.find_element_by_link_text("Mirror").click()
    sleep(5)
    context.driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
    sleep(5)
    # 输入mirror
    context.driver.find_element_by_xpath("//input[@type='text']").click()
    context.driver.find_element_by_xpath("//input[@type='text']").clear()
    context.driver.find_element_by_xpath("//input[@type='text']").send_keys(Mirror)
    sleep(1)
    # 输入desc
    context.driver.find_element_by_xpath("(//input[@type='text'])[2]").click()
    context.driver.find_element_by_xpath("(//input[@type='text'])[2]").clear()
    context.driver.find_element_by_xpath("(//input[@type='text'])[2]").send_keys(Description)
    sleep(1)
    # 点击提交
    context.driver.find_element_by_xpath(
        "//div[@id='app']/div/div[2]/div/div[2]/div[2]/div/div/div/div/form/div[2]/div/button[2]/span").click()



@then('create mirror resultMessage {resultMessage}')
def step_impl(context, resultMessage):
    locator = (By.CSS_SELECTOR, '.el-notification.right>div>h2')
    isCreateSuccess = WebDriverWait(context.driver, 10, 0.5).until(
        EC.text_to_be_present_in_element(locator, resultMessage))
    assert isCreateSuccess == True

@when('delete mirror')
def step_impl(context):
    # 使用URL的方式会出现不显示Create Model 按钮
    # context.driver.get(Url.BASE_URL + Url.MODEL)
    # print("url = " + str(Url.BASE_URL + Url.MODEL))
    sleep(10)
    context.driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/div/div/div/div/ul/li[9]/a/i").click()
    sleep(3)
    context.driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/div/div/div/div/ul/li[9]/a/span").click()
    sleep(1)
    context.driver.find_element_by_link_text("Mirror").click()
    sleep(5)
    context.driver.find_element_by_xpath(
        "//div[@id='app']/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div/div[3]/table/tbody/tr[3]/td[5]/div/button[2]/i").click()
    sleep(1)
    context.driver.find_element_by_xpath("//div[3]/button[2]/span").click()



@then('delete mirror resultMessage {resultMessage}')
def step_impl(context, resultMessage):
    locator = (By.CSS_SELECTOR, '.el-notification.right>div>h2')
    isCreateSuccess = WebDriverWait(context.driver, 10, 0.5).until(
        EC.text_to_be_present_in_element(locator, resultMessage))
    assert isCreateSuccess == True

