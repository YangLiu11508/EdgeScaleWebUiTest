# This Python file uses the following encoding: utf-8
from behave import *
from time import sleep
from constant import Url

@Given('Access Egdescale website')
def step_impl(context):
    context.driver.get(Url.BASE_URL + Url.LOGIN)

@when('login with username {username}, password {password}')
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
    sleep(25)
    print('login end')

@then('There is username {username}')
def step_impl(context, username):
    # nickname = context.driver.find_element_by_xpath("//div[@id='navbar-mobile']/div/div[2]/a/div/span/span")
    # print('get username')
    # if nickname.text == username:
    #     assert True
    # else:
    #     assert False
    context.driver.find_element_by_xpath("//div[@id='navbar-mobile']/div/div[2]/a/div/span/i").click()
    sleep(5)
    context.driver.find_element_by_link_text("Logout").click()
    sleep(10)
