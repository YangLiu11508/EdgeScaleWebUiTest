from behave import *
from time import sleep
from constant import Url


@when('download Solution image')
def step_impl(context):
    context.driver.get(Url.BASE_URL + Url.SOLUTION)
    print("create device url = " + str(Url.BASE_URL + Url.SOLUTION))
    sleep(10)
    context.driver.find_element_by_link_text("Download").click()
