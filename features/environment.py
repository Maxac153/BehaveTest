from behave import fixture
from selenium import webdriver


@fixture
def browser_chrome(context):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--start-maximized")
    context.driver = webdriver.Chrome(options=chrome_options)
    yield context.driver
    context.driver.quit()
