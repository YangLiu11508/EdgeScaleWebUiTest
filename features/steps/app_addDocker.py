from behave import *
from constant import Url
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@when('add docker with Registry {Registry}, imageName {imageName}, Version {Version}')
def step_impl(context,Registry,imageName,Version):
    context.driver.get(Url.BASE_URL + Url.APP)
    print("url = " + str(Url.BASE_URL + Url.APP))
    sleep(15)
    context.driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/div[2]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/button[3]/i").click()
    sleep(5)
    context.driver.find_element_by_xpath(
        "//div[@id='app']/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/a/h6").click()
    sleep(5)
    context.driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
    sleep(7)
    context.driver.find_element_by_xpath("//input[@type='text']").click()
    context.driver.find_element_by_xpath("//input[@type='text']").clear()
    context.driver.find_element_by_xpath("//input[@type='text']").send_keys(Registry)
    sleep(1)
    context.driver.find_element_by_xpath("//div[3]/div/div/ul/li/span[text()= '" + Registry + "']").click()
    sleep(1)
    context.driver.find_element_by_name("image_name").click()
    context.driver.find_element_by_name("image_name").clear()
    context.driver.find_element_by_name("image_name").send_keys(imageName)
    sleep(1)
    context.driver.find_element_by_xpath("(//input[@type='text'])[3]").click()
    context.driver.find_element_by_xpath("(//input[@type='text'])[3]").clear()
    context.driver.find_element_by_xpath("(//input[@type='text'])[3]").send_keys(Version)
    sleep(1)
    context.driver.find_element_by_xpath("//div[4]/div[1]/div[1]/ul/li/span[text()= '" + Version + "']").click()
    sleep(1)
    context.driver.find_element_by_xpath("//div[@id='pane-1']/div/form/div[10]/div/button[4]/span/i").click()



@then('add docker resultMessage {resultMessage}')
def step_impl(context, resultMessage):
    locator = (By.CSS_SELECTOR, '.el-notification.right>div>h2')
    isAddSuccess = WebDriverWait(context.driver, 10, 0.5).until(
        EC.text_to_be_present_in_element(locator, resultMessage))
    assert isAddSuccess == True