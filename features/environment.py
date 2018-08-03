# This Python file uses the following encoding: utf-8
import os
from selenium import webdriver
from time import sleep
from constant import Url

# def before_all(context):
     # print("Executing before all")

def before_feature(context, feature):
     # print("Before feature")

     # 选择浏览器
     # context.driver = webdriver.Chrome()
     # context.driver = webdriver.Firefox()
     context.driver = webdriver.Edge()

     # 判断是否需要登录
     if ('login' != feature.name) and ('login fail' != feature.name) and ('register fail' != feature.name):
         print("-----------------login----------------")
         context.driver.get(Url.BASE_URL + Url.LOGIN)
         context.driver.find_element_by_xpath("//input[@type='text']").click()
         context.driver.find_element_by_xpath("//input[@type='text']").clear()
         context.driver.find_element_by_xpath("//input[@type='text']").send_keys("liu.yang_1@nxp.com")
         context.driver.find_element_by_xpath("//input[@type='password']").click()
         context.driver.find_element_by_xpath("//input[@type='password']").clear()
         context.driver.find_element_by_xpath("//input[@type='password']").send_keys("yangliu123")
         context.driver.find_element_by_xpath("//button[@type='button']").click()
         sleep(10)

def before_scenario(context,scenario):
    # print("Before scenario")
    print(scenario.tags)


def after_scenario(context,scenario):
    try:
        print("scenario status: " + str(scenario.status))
        if scenario.status == "failed":
            if not os.path.exists("./failed_scenarios_screenshots"):
                os.makedirs("./failed_scenarios_screenshots")

            context.driver.save_screenshot("./failed_scenarios_screenshots/" + scenario.name + "_failed.png")

    except Exception as error:
        print('Could not capture the screenshot due to : %s'%(error))

def after_feature(context,feature):
     # print("After feature")
     context.driver.quit()

# def after_all(context):
     # print("Executing after all")
