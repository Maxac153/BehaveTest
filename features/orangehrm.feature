Feature: OrangeHRM Logo
  Scenario: Logo presence on OrangeHRM home Page
    Given launch chrome browser
    When open orange hrm homepage
    Then verify than the logo present on page
    And close browser