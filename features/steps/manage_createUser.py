from behave import *
from constant import Url
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@when('create user with username {username}, email {email}')
def step_impl(context,username,email):
    context.driver.get(Url.BASE_URL + Url.USER)
    print("url = " + str(Url.BASE_URL + Url.USER))
    sleep(10)
    # 输入用户名
    context.driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
    context.driver.find_element_by_xpath("//input[@type='text']").click()
    context.driver.find_element_by_xpath("//input[@type='text']").clear()
    sleep(1)
    # 输入邮箱
    context.driver.find_element_by_xpath("//input[@type='text']").send_keys(username)
    context.driver.find_element_by_xpath("//input[@type='email']").click()
    context.driver.find_element_by_xpath("//input[@type='email']").clear()
    context.driver.find_element_by_xpath("//input[@type='email']").send_keys(email)
    sleep(1)
    # 点击提交
    context.driver.find_element_by_xpath(
        "//div[@id='app']/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/form/div[3]/div/button[2]/span").click()

@then('create user resultMessage {resultMessage}')
def step_impl(context, resultMessage):
    locator = (By.CSS_SELECTOR, 'div.el-message.el-message--success>p')
    isCreateSuccess = WebDriverWait(context.driver, 10, 0.5).until(
        EC.text_to_be_present_in_element(locator,  resultMessage))
    assert isCreateSuccess == True



