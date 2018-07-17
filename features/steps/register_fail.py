# This Python file uses the following encoding: utf-8
from behave import *
from time import sleep
from constant import Url

@Given('register fail Access Egdescale website')
def step_impl(context):
    context.driver.get(Url.BASE_URL + Url.REGISTER)

@when('register fail with FirstName {FirstName}, LastName {LastName}, Email {Email}, AccountType {AccountType}, CompanyName {CompanyName}')
def step_impl(context, FirstName, LastName,Email,AccountType,CompanyName):
    context.driver.find_element_by_xpath("//input[@type='text']").click()
    context.driver.find_element_by_xpath("//input[@type='text']").clear()
    context.driver.find_element_by_xpath("//input[@type='text']").send_keys(FirstName)
    sleep(5)
    context.driver.find_element_by_xpath("(//input[@type='text'])[2]").click()
    context.driver.find_element_by_xpath("(//input[@type='text'])[2]").clear()
    context.driver.find_element_by_xpath("(//input[@type='text'])[2]").send_keys(LastName)
    sleep(5)
    context.driver.find_element_by_xpath("//input[@type='email']").click()
    context.driver.find_element_by_xpath("//input[@type='email']").clear()
    context.driver.find_element_by_xpath("//input[@type='email']").send_keys(Email)
    sleep(5)
    context.driver.find_element_by_xpath("(//input[@type='text'])[4]").click()
    context.driver.find_element_by_xpath("(//input[@type='text'])[4]").clear()
    context.driver.find_element_by_xpath("(//input[@type='text'])[4]").send_keys(CompanyName)
    sleep(5)
    context.driver.find_element_by_xpath("//button[@type='button']").click()
    sleep(10)

@then('stay in register page')
def step_impl(context):
    pageUrl = context.driver.current_url
    if pageUrl == Url.BASE_URL + Url.REGISTER:
        return True
    else:
        return False
