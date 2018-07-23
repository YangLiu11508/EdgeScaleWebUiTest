from behave import *
from time import sleep
import os
from constant import Url
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@when('create app with dockerName {dockerName}, vendor {vendor}, appIcon {appIcon}, registry {registry}, imageName {imageName}, version {version}')
def step_impl(context, dockerName, vendor, appIcon, registry, imageName, version):
    context.driver.get(Url.BASE_URL + Url.APP_CREATE)
    print("url = " + str(Url.BASE_URL + Url.APP_CREATE))
    sleep(15)
    context.driver.find_element_by_name("name").click()
    context.driver.find_element_by_name("name").clear()
    context.driver.find_element_by_name("name").send_keys(dockerName)
    context.driver.find_element_by_xpath(
        "//div[@id='app']/div/div[2]/div/div[2]/div[2]/div/div/div/div/div[2]/form/div/div[3]/div/div/div/i").click()
    context.driver.find_element_by_xpath(
        "//div[@id='app']/div/div[2]/div/div[2]/div[2]/div/div/div/div/div[2]/form/div/div[3]/div/div[2]/div/div[2]/div").click()
    sleep(5)
    upload = context.driver.find_element_by_xpath("//input[@type='file']")
    context.driver.execute_script("arguments[0].style.display = 'block';", upload)
    upload = context.driver.find_element_by_xpath("//input[@type='file']")
    appIconUrl = os.path.abspath('..') + '\\' + appIcon
    print("appImageUrl = " + appIconUrl)
    upload.send_keys(appIconUrl)
    sleep(5)
    context.driver.find_element_by_link_text("Save").click()
    sleep(5)
    context.driver.find_element_by_xpath(
        "//div[@id='app']/div/div[2]/div/div[2]/div[2]/div/div/div/div/div[2]/form/div[2]/div/button[2]/span/i").click()
    context.driver.find_element_by_xpath("//input[@type='text']").click()
    context.driver.find_element_by_xpath("//input[@type='text']").clear()
    context.driver.find_element_by_xpath("//input[@type='text']").send_keys(registry)
    sleep(5)
    context.driver.find_element_by_xpath("//div[3]/div/div/ul/li/span").click()
    sleep(5)
    context.driver.find_element_by_name("image_name").click()
    context.driver.find_element_by_name("image_name").clear()
    context.driver.find_element_by_name("image_name").send_keys(imageName)
    context.driver.find_element_by_xpath("(//input[@type='text'])[3]").click()
    context.driver.find_element_by_xpath("(//input[@type='text'])[3]").clear()
    context.driver.find_element_by_xpath("(//input[@type='text'])[3]").send_keys(version)
    sleep(5)
    context.driver.find_element_by_xpath("//div[4]/div/div/ul/li/span").click()
    context.driver.find_element_by_xpath(
        "//div[@id='app']/div/div[2]/div/div[2]/div[2]/div/div/div/div/div[2]/form/div[2]/div/button[3]/span").click()
    sleep(10)

@then('Jump to the app list page')
def step_impl(context):
    pageUrl = context.driver.current_url
    if pageUrl == Url.BASE_URL + Url.APP:
        return True
    else:
        return False


@when('delete app with appName {appName}')
def step_impl(context, appName):
    context.driver.get(Url.BASE_URL + Url.APP)
    print("device list url = " + str(Url.BASE_URL + Url.APP))
    sleep(10)
    # context.driver.find_element_by_xpath(
    #     "//div[@id='app']/div/div[2]/div/div[2]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/button[3]/i").click()
    # sleep(5)
    # rowElement = context.driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/div/div[2]/div")
    # rows = rowElement.find_elements_by_xpath(".//div[contains(@class,'col-md-4')]")
    # for i in rows:
    #     titleElement = i.find_element_by_xpath(".//div/div/a/h6")
    #     if appName in titleElement.text:
    #         titleElement.find_element_by_xpath("./../following-sibling::div[6]/div/button[1]").click()
    #         sleep(5)
    #         context.driver.find_element_by_xpath("//div[@id='modal_theme_warning']/div/div/div[3]/button[2]").click()
    #         sleep(5)
    #         break
    context.driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/div[2]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/button[3]/i").click()
    sleep(5)
    context.driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div[6]/div/button/span").click()
    sleep(5)
    context.driver.find_element_by_xpath("//div[@id='modal_theme_warning']/div/div/div[3]/button[2]").click()


@then('delete app resultMessage {resultMessage}')
def step_impl(context, resultMessage):
    locator = (By.CSS_SELECTOR, '.el-notification.right>div>h2')
    isDeleteSuccess = WebDriverWait(context.driver, 10, 0.5).until(
        EC.text_to_be_present_in_element(locator, resultMessage))
    assert isDeleteSuccess == True
