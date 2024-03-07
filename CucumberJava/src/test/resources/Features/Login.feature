Feature: Sample login functionality

  Scenario Outline: check valid login
    Given user has given the login page
    When user gives valid <username> <password>
    And clicks login
    Then user should be navigated to home page

    Examples: 
      | username | password             |
      | practice | SuperSecretPassword! |
      | practice | superdup             |
