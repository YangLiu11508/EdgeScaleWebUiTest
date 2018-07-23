# This Python file uses the following encoding: utf-8
from behave import *
from time import sleep
from constant import Url
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@when('change password with OldPassword {OldPassword}, Password {Password}')
def step_impl(context, OldPassword, Password):
    sleep(10)
    context.driver.find_element_by_xpath("//div[@id='navbar-mobile']/div/div[2]/a/div/span/span").click()
    sleep(5)
    context.driver.find_element_by_link_text("Account settings").click()
    sleep(5)
    context.driver.find_element_by_xpath("//input[@type='password']").click()
    context.driver.find_element_by_xpath("//input[@type='password']").clear()
    context.driver.find_element_by_xpath("//input[@type='password']").send_keys(OldPassword)
    sleep(5)
    context.driver.find_element_by_xpath("(//input[@type='password'])[2]").click()
    context.driver.find_element_by_xpath("(//input[@type='password'])[2]").clear()
    context.driver.find_element_by_xpath("(//input[@type='password'])[2]").send_keys(Password)
    sleep(5)
    context.driver.find_element_by_xpath("(//input[@type='password'])[3]").click()
    context.driver.find_element_by_xpath("(//input[@type='password'])[3]").clear()
    context.driver.find_element_by_xpath("(//input[@type='password'])[3]").send_keys(Password)
    sleep(5)
    context.driver.find_element_by_xpath("//div[@id='app']/div/div/div/div[2]/div/div[3]/span/button[2]/span").click()
    sleep(5)

    # 登出
    context.driver.find_element_by_xpath("//div[@id='navbar-mobile']/div/div[2]/a/div/span/span").click()
    sleep(5)
    context.driver.find_element_by_link_text("Logout").click()
    sleep(10)
    # 登录
    context.driver.find_element_by_xpath("//input[@type='text']").click()
    context.driver.find_element_by_xpath("//input[@type='text']").clear()
    context.driver.find_element_by_xpath("//input[@type='text']").send_keys("liu.yang_1@nxp.com")
    print('send username')
    context.driver.find_element_by_xpath("//input[@type='password']").click()
    context.driver.find_element_by_xpath("//input[@type='password']").clear()
    context.driver.find_element_by_xpath("//input[@type='password']").send_keys(Password)
    print('send password')
    context.driver.find_element_by_xpath("//button[@type='button']").click()
    sleep(25)
    # 把密码改回原来的
    context.driver.find_element_by_xpath("//div[@id='navbar-mobile']/div/div[2]/a/div/span/span").click()
    sleep(5)
    context.driver.find_element_by_link_text("Account settings").click()
    sleep(5)
    context.driver.find_element_by_xpath("//input[@type='password']").click()
    context.driver.find_element_by_xpath("//input[@type='password']").clear()
    context.driver.find_element_by_xpath("//input[@type='password']").send_keys(Password)
    sleep(5)
    context.driver.find_element_by_xpath("(//input[@type='password'])[2]").click()
    context.driver.find_element_by_xpath("(//input[@type='password'])[2]").clear()
    context.driver.find_element_by_xpath("(//input[@type='password'])[2]").send_keys(OldPassword)
    sleep(5)
    context.driver.find_element_by_xpath("(//input[@type='password'])[3]").click()
    context.driver.find_element_by_xpath("(//input[@type='password'])[3]").clear()
    context.driver.find_element_by_xpath("(//input[@type='password'])[3]").send_keys(OldPassword)
    sleep(5)
    context.driver.find_element_by_xpath("//div[@id='app']/div/div/div/div[2]/div/div[3]/span/button[2]/span").click()


@then('change password with resultMessage {resultMessage}')
def step_impl(context,resultMessage):
    locator = (By.CSS_SELECTOR, 'div.el-message.el-message--success>p')
    isDeleteSuccess = WebDriverWait(context.driver, 10, 0.5).until(
        EC.text_to_be_present_in_element(locator, resultMessage))
    assert isDeleteSuccess == True

