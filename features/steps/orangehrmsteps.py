import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('launch chrome browser')
def launch_browser(context):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--start-maximized")
    context.driver = webdriver.Chrome(options=chrome_options)


@when('open orange hrm homepage')
def step_impl(context):
    context.driver.get("https://www.google.com/")


@then('verify than the logo present on page')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//textarea').send_keys('12546465465')


@then('close browser')
def step_impl(context):
    time.sleep(5)
    context.driver.close()
    context.driver.quit()

