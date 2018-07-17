from behave import *
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from constant import Url

@given('None')
def step_impl(context):
    return

@when('create device with SN {sn}, modelName {modelName}')
def step_impl(context, sn, modelName):
    context.driver.get(Url.BASE_URL + Url.DEVICE_CREATE)
    print("create device url = " + str(Url.BASE_URL + Url.DEVICE_CREATE))
    sleep(10)
    context.driver.find_element_by_name("fuid").click()
    context.driver.find_element_by_name("fuid").clear()
    context.driver.find_element_by_name("fuid").send_keys(sn)
    context.driver.find_element_by_xpath("//form[@id='createIdHost']/div[2]/div/div/button/span").click()
    sleep(5)
    context.driver.find_element_by_xpath("(//input[@type='text'])[3]").click()
    context.driver.find_element_by_xpath("(//input[@type='text'])[3]").clear()
    context.driver.find_element_by_xpath("(//input[@type='text'])[3]").send_keys(modelName)
    sleep(5)
    context.driver.find_element_by_xpath("//ul/li/span[text()= '" + modelName + "']").click()
    sleep(5)
    context.driver.find_element_by_xpath("//form[@id='createHost']/div[3]/div/div/button/span").click()
    sleep(5)

@when('delete device with deviceName {deviceName}')
def step_impl(context, deviceName):
    context.driver.get(Url.BASE_URL + Url.DEVICE)
    print("device list url = " + str(Url.BASE_URL + Url.DEVICE))
    sleep(5)
    parentBtn = context.driver.find_element_by_xpath(
        '//div[1]/div[1]/div/h6/div/div[1]/a/span[contains(text(), "#' + deviceName + '")]/../../../../../../../..')
    parentBtn.find_element_by_link_text("Delete").click()
    sleep(5)
    context.driver.find_element_by_xpath('//*[@id="modal_theme_warning"]/div/div/div[3]/button[2]').click()


@then("create resultMessage {resultMessage}")
def step_impl(context, resultMessage):
    element = context.driver.find_element_by_xpath(
        "//div[@id='app']/div/div[2]/div/div[2]/div[2]/div[1]/div/div[3]/div/div[1]/span")
    if element.text == resultMessage:
        assert True
    else:
        assert False

@then("delete device resultMessage {resultMessage}")
def step_impl(context, resultMessage):
    locator = (By.CSS_SELECTOR, '.el-notification.right>div>h2')
    isDeleteSuccess = WebDriverWait(context.driver, 10, 0.5).until(
        EC.text_to_be_present_in_element(locator, resultMessage))
    assert isDeleteSuccess == True
