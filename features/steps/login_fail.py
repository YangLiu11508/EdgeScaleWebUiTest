# This Python file uses the following encoding: utf-8
from behave import *
from time import sleep
from constant import Url

@Given('login fail Access Egdescale website')
def step_impl(context):
    context.driver.get(Url.BASE_URL + Url.LOGIN)

@when('login fail with username {username}, password {password}')
def step_impl(context, username, password):
    print('login start')
    context.driver.find_element_by_xpath("//input[@type='text']").click()
    context.driver.find_element_by_xpath("//input[@type='text']").clear()
    context.driver.find_element_by_xpath("//input[@type='text']").send_keys(username)
    print('send username')
    context.driver.find_element_by_xpath("//input[@type='password']").click()
    context.driver.find_element_by_xpath("//input[@type='password']").clear()
    context.driver.find_element_by_xpath("//input[@type='password']").send_keys(password)
    print('send password')
    context.driver.find_element_by_xpath("//button[@type='button']").click()
    sleep(10)
    print('login end')

@then('stay in login page')
def step_impl(context):
    pageUrl = context.driver.current_url
    if pageUrl == Url.BASE_URL + Url.LOGIN:
        return True
    else:
        return False
