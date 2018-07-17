from behave import *
from time import sleep
from constant import Url


@when('find model with vendor {vendor}')
def step_impl(context, vendor):
    context.driver.get(Url.BASE_URL + Url.MODEL)
    print("create device url = " + str(Url.BASE_URL + Url.MODEL))
    sleep(10)
    context.driver.find_element_by_xpath("(//input[@type='search'])[4]").click()
    context.driver.find_element_by_xpath("(//input[@type='search'])[4]").clear()
    context.driver.find_element_by_xpath("(//input[@type='search'])[4]").send_keys(vendor)
    sleep(1)
    context.driver.find_element_by_xpath("(//button[@type='button'])[3]").click()