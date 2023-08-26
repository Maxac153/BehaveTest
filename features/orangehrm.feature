Feature: Регистрация пользователя
  Background: Нахожусь на странице регистрации
    Given Открываем сайт "http://users.bugred.ru/user/login/index.html"
  @fixture.browser.chrome
  Scenario: Пользователь вводит данные для регистрации
    When Ввести имя пользователя "tur123"
    And Ввести Email пользователя "verygoodnice@gmail.com"
    And Ввести Пароль пользователя "123"
    And Нажать кнопку Зарегистрироваться
    Then Проверяем что пользователь зарегистрирован успешно "tur123"