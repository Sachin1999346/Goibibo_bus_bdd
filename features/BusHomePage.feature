Feature: Bus Home Page

  Background: common method
    Given open the browser and enter the valid url
    When click on bus button

  Scenario: User should be click on bus button Successfully
    Then Verify bus page is displayed

  Scenario Outline: User Enter the valid source and destination in from and to
    When Enter the From "<from_location>"
    And Click on To Testfiled and Enter the Destination "<to_location>"
    Then Verify is displayed
    Examples:
      | from_location | to_location |
      | Wakad         | Majestic    |

  Scenario: User Should be able to click on Today or Tomorrow button
    When User click on Today date Button
    And User click on Tomorrow date Button
    Then Verify that is clickable

  Scenario: User Should be click on any Today Onward Date
    When click on Travel Date
    And click on next month Arrow button
    And select any today onward date
    Then Verify that is select and displayed

  Scenario Outline:user should be click on search bus button
    When click on from textfield and enter source "<from_location>"
    And enter the destination "<to_location>" into To Textfield
    And select the date
    And click on Search Bus button
    Then Verify it navigate to next page

    Examples:
      | from_location | to_location |
      | Wakad         | majestic    |


