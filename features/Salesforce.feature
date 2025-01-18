Feature: Salesforce Final Project

  @smoke
  Scenario Outline: Use Case 1
    Given Open Salesforce page and verify title
    When Login with username and password
    When Create a lead with details: "<salutation>", "<first_name>", "<last_name>", "<company>"
    Then Verify lead has created
    When Convert the lead to account by creating new account from lead to account convert page
    Then Verify lead has converted successfully
    When Create a account with details: "<account_name>"
    Then Verify account: "<account_name>" has created
    When Create a lead with details: "Mr.", "Nova", "Klan", "MN Steel"
    Then Verify lead has created
    When Convert the lead to account and use existing account: "<account_name>"
    Then Verify lead has converted successfully
    Then Remove or Delete the account
    Then Remove or Delete the account

    Examples:
      | salutation | first_name | last_name | company     | account_name |
      | Mr.        | Robert     | Twin      | Example Inc | Acme         |


  @smoke
  Scenario Outline: Use Case 2
    Given Open Salesforce page and verify title
    When Login with username and password
    When Create a account with details: "<account_name>"
    Then Verify account: "<account_name>" has created
    When Create a contact with details: "<salutation>", "<first_name>", "<last_name>" and attach "<account_name>"
    Then Verify contact: "<contact_name>" has saved successfully with "<account_name>"
    When Create a opportunity with details: "<opportunity_name>", "<close_date>", "<stage>", "<forecast_category>" and attach "<account_name>"
    Then Verify opportunity: "<opportunity_name>" has saved successfully with "<account_name>"
    Then Remove or Delete the account

    Examples:
      | salutation | first_name | last_name | account_name | opportunity_name | close_date | stage   | forecast_category | contact_name |
      | Mr.        | Zoya       | B         | Acme         | Zaya Opp         | 02/2/2025  | Propose | Pipeline          | Zoya B       |


  @smoke
  Scenario Outline: Use Case 3 (Create an event in the calendar page for any account)
    Given Open Salesforce page and verify title
    When Login with username and password
    When Create new event with subject: "<event_name>"
    Then Verify event: "<event_name>" has added
    Then click on logout

    Examples:
      | event_name |
      | Call       |