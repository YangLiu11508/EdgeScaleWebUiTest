from behave import *
from constant import Url
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@when('create model with Model {Model}, Type {Type}, Platform {Platform}, Vendor {Vendor}')
def step_impl(context,Model,Type,Platform,Vendor):
    # 使用URL的方式会出现不显示Create Model 按钮
    # context.driver.get(Url.BASE_URL + Url.MODEL)
    # print("url = " + str(Url.BASE_URL + Url.MODEL))
    sleep(10)
    context.driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/div/div/div/div/ul/li[4]/a/i").click()
    sleep(5)
    context.driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/div/div/div/div/ul/li[4]/a/span").click()
    sleep(2)
    context.driver.find_element_by_link_text("Model List").click()
    sleep(5)
    context.driver.find_element_by_xpath(
        "//div[@id='app']/div/div[2]/div/div[2]/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div/button/i").click()
    sleep(5)
    # 输入并点击Model
    context.driver.find_element_by_xpath("//input[@type='text']").click()
    context.driver.find_element_by_xpath("//input[@type='text']").clear()
    context.driver.find_element_by_xpath("//input[@type='text']").send_keys(Model)
    sleep(2)
    context.driver.find_element_by_xpath("//div[3]/div[1]/div[1]/ul/li/span[text()= '" + Model + "']").click()
    sleep(1)
    # 选择Type
    context.driver.find_element_by_xpath("(//input[@type='text'])[2]").click()
    sleep(2)
    context.driver.find_element_by_xpath("//div[4]/div[1]/div[1]/ul/li/span[text()= '" + Type + "']").click()
    sleep(1)
    # 选择Platform
    context.driver.find_element_by_xpath("(//input[@type='text'])[3]").click()
    sleep(1)
    context.driver.find_element_by_xpath("//div[5]/div[1]/div[1]/ul/li/span[text()= '" + Platform + "']").click()
    sleep(1)
    # 输入并点击Vendor
    context.driver.find_element_by_xpath("(//input[@type='text'])[4]").click()
    context.driver.find_element_by_xpath("(//input[@type='text'])[4]").clear()
    context.driver.find_element_by_xpath("(//input[@type='text'])[4]").send_keys(Vendor)
    sleep(1)
    context.driver.find_element_by_xpath("//div[6]/div/div/ul/li/span[text()= '" + Vendor + "']").click()
    sleep(1)
    context.driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/div[2]/div[2]/div/div/form/fieldset/form/div[5]/div/div/label/span/span").click()
    context.driver.find_element_by_xpath("(//button[@type='button'])[3]").click()

@then('create model resultMessage {resultMessage}')
def step_impl(context, resultMessage):
    locator = (By.CSS_SELECTOR, '.el-notification.right>div>h2')
    isCreateSuccess = WebDriverWait(context.driver, 10, 0.5).until(
        EC.text_to_be_present_in_element(locator, resultMessage))
    assert isCreateSuccess == True



@when('edit model with Model {Model}, Type {Type}, Platform {Platform}, Vendor {Vendor}')
def step_impl(context,Model,Type,Platform,Vendor):
    # 使用URL的方式会出现不显示Create Model 按钮
    # context.driver.get(Url.BASE_URL + Url.MODEL)
    # print("url = " + str(Url.BASE_URL + Url.MODEL))
    sleep(10)
    context.driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/div/div/div/div/ul/li[4]/a/i").click()
    sleep(5)
    context.driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/div/div/div/div/ul/li[4]/a/span").click()
    sleep(2)
    context.driver.find_element_by_link_text("Model List").click()
    sleep(5)
    context.driver.find_element_by_link_text("Edit model").click()
    sleep(5)
    # 输入并点击Model
    context.driver.find_element_by_xpath("//input[@type='text']").click()
    context.driver.find_element_by_xpath("//input[@type='text']").clear()
    context.driver.find_element_by_xpath("//input[@type='text']").send_keys(Model)
    sleep(2)
    context.driver.find_element_by_xpath("//div[3]/div[1]/div[1]/ul/li/span[text()= '" + Model + "']").click()
    sleep(1)
    # 选择Type
    context.driver.find_element_by_xpath("(//input[@type='text'])[2]").click()
    context.driver.find_element_by_xpath("(//input[@type='text'])[2]").clear()
    sleep(2)
    context.driver.find_element_by_xpath("//div[4]/div[1]/div[1]/ul/li/span[text()= '" + Type + "']").click()
    sleep(1)
    # 选择Platform
    context.driver.find_element_by_xpath("(//input[@type='text'])[3]").click()
    context.driver.find_element_by_xpath("(//input[@type='text'])[3]").clear()
    sleep(1)
    context.driver.find_element_by_xpath("//div[5]/div[1]/div[1]/ul/li/span[text()= '" + Platform + "']").click()
    sleep(1)
    # 输入并点击Vendor
    context.driver.find_element_by_xpath("(//input[@type='text'])[4]").click()
    context.driver.find_element_by_xpath("(//input[@type='text'])[4]").clear()
    context.driver.find_element_by_xpath("(//input[@type='text'])[4]").send_keys(Vendor)
    sleep(1)
    context.driver.find_element_by_xpath("//div[6]/div/div/ul/li/span[text()= '" + Vendor + "']").click()
    sleep(1)
    context.driver.find_element_by_xpath("(//button[@type='button'])[3]").click()

@then('edit model resultMessage {resultMessage}')
def step_impl(context, resultMessage):
    locator = (By.CSS_SELECTOR, '.el-notification.right>div>h2')
    isEditSuccess = WebDriverWait(context.driver, 10, 0.5).until(
        EC.text_to_be_present_in_element(locator, resultMessage))
    assert isEditSuccess == True



@when('delete model')
def step_impl(context):
    # 使用URL的方式会出现不显示Create Model 按钮
    # context.driver.get(Url.BASE_URL + Url.MODEL)
    # print("url = " + str(Url.BASE_URL + Url.MODEL))
    sleep(10)
    context.driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/div/div/div/div/ul/li[4]/a/i").click()
    sleep(2)
    context.driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/div/div/div/div/ul/li[4]/a/span").click()
    sleep(2)
    context.driver.find_element_by_link_text("Model List").click()
    sleep(5)
    context.driver.find_element_by_link_text("Delete model").click()
    sleep(2)
    context.driver.find_element_by_xpath("(//button[@type='button'])[17]").click()

@then('delete model resultMessage {resultMessage}')
def step_impl(context, resultMessage):
    locator = (By.CSS_SELECTOR, '.el-notification.right>div>h2')
    isDeleteSuccess = WebDriverWait(context.driver, 10, 0.5).until(
        EC.text_to_be_present_in_element(locator, resultMessage))
    assert isDeleteSuccess == True