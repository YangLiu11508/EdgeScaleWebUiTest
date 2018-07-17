from behave import *
from time import sleep
from constant import Url


@when('find model with plantform {plantform}')
def step_impl(context, plantform):
    context.driver.get(Url.BASE_URL + Url.MODEL)
    print("create device url = " + str(Url.BASE_URL + Url.MODEL))
    sleep(10)
    context.driver.find_element_by_xpath("(//input[@type='search'])[3]").click()
    context.driver.find_element_by_xpath("(//input[@type='search'])[3]").clear()
    context.driver.find_element_by_xpath("(//input[@type='search'])[3]").send_keys(plantform)
    sleep(1)
    context.driver.find_element_by_xpath("(//button[@type='button'])[3]").click()