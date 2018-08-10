from behave import *
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from constant import Url

@when("create solution with name {solutionName}, modelName {modelName}, version {version}, tagName {tagName}, imageUrl {imageUrl}")
def step_impl(context, solutionName, modelName, version, tagName,imageUrl):
    context.driver.get(Url.BASE_URL + Url.SOLUTION_CREATE)
    sleep(10)
    context.driver.find_element_by_xpath("//input[@type='text']").click()
    context.driver.find_element_by_xpath("//input[@type='text']").clear()
    context.driver.find_element_by_xpath("//input[@type='text']").send_keys(modelName)
    sleep(5)
    context.driver.find_element_by_xpath("//ul/li/span[text()= '" + modelName + "']").click()
    sleep(5)
    context.driver.find_element_by_xpath("(//input[@type='text'])[2]").click()
    context.driver.find_element_by_xpath("(//input[@type='text'])[2]").clear()
    context.driver.find_element_by_xpath("(//input[@type='text'])[2]").send_keys(solutionName)
    context.driver.find_element_by_xpath("(//input[@type='text'])[3]").click()
    context.driver.find_element_by_xpath("(//input[@type='text'])[3]").clear()
    context.driver.find_element_by_xpath("(//input[@type='text'])[3]").send_keys(version)
    sleep(5)
    context.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='nxp--arm64--generic--lsdk'])[1]/following::span[2]").click()
    sleep(5)
    context.driver.find_element_by_xpath(
        "//div[@id='app']/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/form/div[2]/div/button[2]/span").click()
    sleep(5)
    context.driver.find_element_by_xpath("(//input[@type='text'])[2]").click()
    context.driver.find_element_by_xpath("//input[@type='text']").clear()
    context.driver.find_element_by_xpath("//input[@type='text']").send_keys(tagName)
    sleep(5)
    context.driver.find_element_by_xpath("//ul/li/span[text()= '" + tagName +"']").click()
    sleep(5)
    context.driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/form").click()
    sleep(5)
    context.driver.find_element_by_xpath(
        "//div[@id='app']/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/form/div[2]/div/button[3]/span").click()
    context.driver.find_element_by_xpath("//input[@type='text']").click()
    context.driver.find_element_by_xpath("//input[@type='text']").clear()
    context.driver.find_element_by_xpath("//input[@type='text']").send_keys(imageUrl)
    context.driver.find_element_by_xpath(
        "//div[@id='app']/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/form/div[2]/div/button[3]/span").click()

@then("create solution with resultMessage {resultMessage}")
def step_impl(context, resultMessage):
    locator = (By.CSS_SELECTOR, '.el-notification.right>div>h2')
    isDeleteSuccess = WebDriverWait(context.driver, 10, 0.5).until(
        EC.text_to_be_present_in_element(locator, resultMessage))
    assert isDeleteSuccess == True

@when("delete solution with solutionName {solutionName}")
def step_impl(context, solutionName):
    context.driver.get(Url.BASE_URL + Url.SOLUTION)
    sleep(5)
    parentBtn = context.driver.find_element_by_xpath(
        '//div/div/div[1]/h6/a[contains(text(), "# ' + solutionName + '")]/../../../../..')
    parentBtn.find_element_by_link_text("Delete").click()
    sleep(5)
    context.driver.find_element_by_xpath('//*[@id="modal_theme_warning"]/div/div/div[3]/button[2]').click()

@then("delete solution with resultMessage {resultMessage}")
def step_impl(context, resultMessage):
    locator = (By.CSS_SELECTOR, '.el-notification.right>div>h2')
    isDeleteSuccess = WebDriverWait(context.driver, 10, 0.5).until(
        EC.text_to_be_present_in_element(locator, resultMessage))
    assert isDeleteSuccess == True
    sleep(10)
