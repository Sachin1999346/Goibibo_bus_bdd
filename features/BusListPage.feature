Feature: Bus List Page

  Background: common method
    Given open the browser and enter the URL
    When click on bus button and open bus page
    And click on from and enter source "Wakad"
    And click on to destination "Majestic" into To Textfield
    And select the required Date
    And click on Search Bus Button then bus list page open

  Scenario: User Should be click on Multiple CheckBox and Reset button on filter
    When click on multiple Check box and Reset Button on popular Filter
    And click on multiple Check box and Reset Button on Bus Type Filter
    And click on multiple Check box and Reset Button on Arrival Time Filter
    And click on search textfield on Boarding point filter
    And click on All Boarding Point Option
    And click on multiple Check box and Reset Button on Boarding Point Filter
    And click on search textfield on Dropping point filter
    And click on All Dropping point Option
    And click on multiple Check box and Reset Button on Dropping point Filter
    And click on search textfield on Bus Operator filter
    And click on All Bus Operator Option
    And click on multiple Check box and Reset Button on Bus Operator Filter
    And click on All Bus Amenities Option
    And click on multiple Check box and Reset Button on Amenities Filter
    Then Verify it is clickable and displayed

  Scenario: User should be able to select seat,boarding time and Dropping time.
    When click on select seat button
    And click on boarding point time radio button
    And click on dropping point time radio button
    And click on available seat
    And click on continue button
    Then verify is clickable and navigate review your booking page

  Scenario Outline:User should be provide personal details.
    When click on select seat button
    And click on boarding point time radio button
    And click on dropping point time radio button
    And click on available seat
    And click on continue button
    And click on yes radio button for Trip Insurance
    And click on No radio button for Trip Insurance
    And click on full name and provide Traveller "<full_name>"
    And Enter Traveller Age in "<age>" textfield
    And click on male or female "<gender>"
    And Enter Traveller Email "<email_id>"
    And Enter Traveller Mobile Number "<mobile_number>"
    And click on Pay button
    Then Verify and is navigate to new all payment mode page
    Examples:
      | full_name          | age | gender | email_id            | mobile_number |
      | Sachin Ramdas Gore | 23  | Male   | sgore9240@gmail.com | 9657063172    |
      | Saurbh123 patil    | 24  | Male   | saurbh456@gmail.com | 9657063       |
      | pankaj patil       | 25  | Male   | pankajpatil256.com  | 9021449098    |


  Scenario Outline:user should be able to do payment
    When click on select seat button
    And click on boarding point time radio button
    And click on dropping point time radio button
    And click on available seat
    And click on continue button
    And click on No radio button for Trip Insurance
    And click on full name and provide Traveller "Sachin Ramdas Gore"
    And Enter Traveller Age in "23" textfield
    And click on male or female "male"
    And Enter Traveller Email "sachingore654@gmail.com"
    And Enter Traveller Mobile Number "9657063172"
    And click on Pay button
    And click on credit and debit card mode
    And enter the card Number "<card_number>"
    And click on month
    And click on year
    And enter the cvv "<cvv>"
    And enter name on card "<card_name>"
    And click on save and pay button
    Then verify otp send to given mobile number and enter OTP Page displayed

    Examples:
      | card_number      | cvv | card_name          |
      | 4592000191311337 | 123 | Sachin Ramdas Gore |
      | 45920001913      | 123 | Sachin Ramdas Gore |
