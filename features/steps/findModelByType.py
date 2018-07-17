from behave import *
from time import sleep
from constant import Url


@when('find model with type {type}')
def step_impl(context, type):
    context.driver.get(Url.BASE_URL + Url.MODEL)
    print("create device url = " + str(Url.BASE_URL + Url.MODEL))
    sleep(10)
    context.driver.find_element_by_xpath("(//input[@type='search'])[2]").click()
    context.driver.find_element_by_xpath("(//input[@type='search'])[2]").clear()
    context.driver.find_element_by_xpath("(//input[@type='search'])[2]").send_keys(type)
    sleep(1)
    context.driver.find_element_by_xpath("(//button[@type='button'])[3]").click()