from behave import given, when, then
from selenium import webdriver


@given('Открываем сайт "{url}"')
def step_launch_browser(context, url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--start-maximized")
    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.get(url)


@when('Ввести имя пользователя "{user_name}"')
def step_input_user_name(context, user_name):
    context.driver.find_element('xpath', '//input[@name="name"]').send_keys(user_name)


@when('Ввести Email пользователя "{email}"')
def step_input_user_email(context, email):
    context.driver.find_element('xpath', '//input[@required=""][@name="email"]').send_keys(email)


@when('Ввести Пароль пользователя "{password}"')
def step_input_user_password(context, password):
    context.driver.find_element('xpath', '//input[@required=""][@name="password"]').send_keys(password)


@when('Нажать кнопку Зарегистрироваться')
def step_clicked_button_registration(context):
    context.driver.find_element('xpath', '//input[@value="Зарегистрироваться"]').click()


@then('Проверяем что пользователь зарегистрирован успешно "{extended_result}"')
def step_check_result(context, extended_result):
    result = context.driver.find_element('xpath', '//a[@class="dropdown-toggle"]').text
    assert extended_result == result
    context.driver.quit()
