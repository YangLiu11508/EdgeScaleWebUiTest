from behave import *
from time import sleep
from constant import Url


@when('find model with Model {Model}')
def step_impl(context, Model):
    context.driver.get(Url.BASE_URL + Url.MODEL)
    print("create device url = " + str(Url.BASE_URL + Url.MODEL))
    sleep(10)
    context.driver.find_element_by_xpath("//input[@type='search']").click()
    context.driver.find_element_by_xpath("//input[@type='search']").clear()
    context.driver.find_element_by_xpath("//input[@type='search']").send_keys(Model)
    sleep(1)
    context.driver.find_element_by_xpath("(//button[@type='button'])[3]").click()