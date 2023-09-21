@web @module:login
@storyId:TS-001
Feature: Login Screen and Login Functionality

  Background: precondition
    # Background is optional and can be used for precondition, if any
    Given COMMENT: 'setup done!'

  @testcaseId:TC-001
  Scenario: User is able to login successfully
    Given user navigates to login screen
    When login using '${valid.user.email}' and '${valid.user.password}'
    Then verify login password error is ''
    Then verify ${valid.user.email} successfully logged in

  Scenario Outline: login form should display error for invalid entry - with examples
    Given user navigates to login screen
    When login using '<username>' and '<password>'
    Then verify login username error is '<username-error>'
    And verify login password error is '<pwd-error>'
    And verify login form error is '<gen-error>'

    Examples:
    |testcaseId| username| password| summary| username-error| pwd-error| gen-error|
    |TC-002    |||blank user and pwd| Please enter username | Please enter password    |     |
    |TC-003    |test     ||blank pwd| | Please enter password| |
    |TC-004||test|blank user| Please enter username| | |
    |TC-005|test|test|wrong user or pwd|||Wrong username or password, please try again!...|

  #Sample data driven scenario with external test data
  @datafile:resources/data/logindata.csv
  Scenario: login form should display error for invalid entry
    Given user navigates to login screen
    When login using '<username>' and '<password>'
    Then verify login username error is '<username-error>'
    And verify login password error is '<pwd-error>'
    And verify login form error is '<gen-error>'

  #@step
  Step-def: verify login password error is '{message}'
    Then verify 'loginpage.password-error.loc' error is '${message}'
    