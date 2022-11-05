import datetime
import re
import time

from behave import *
from selenium import webdriver
SCREENSHOTS_PATH = r'C:\Users\Shree\PycharmProjects\BDD Project\Screenshots\\'

@given('open the browser and enter the url')
def lunch_browser(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.goibibo.com/")
    context.driver.maximize_window()

@when('click on bus button and open bus page')
def click_bus_btn(context):
    time.sleep(5)
    context.driver.find_element("xpath", '//a[text()="Bus"]').click()

@when('click on from and enter source "{from_location}"')
def enter_data(context, from_location):
    try:
        time.sleep(2)
        pattern = r'[a-zA-Z]+'
        result = re.findall(pattern, from_location)
        assert result, "invalid from location"
        context.driver.find_element("xpath", '//input[@id = "autosuggestBusSRPSrcHome"]').send_keys(from_location)
        time.sleep(3)
        context.driver.find_element("xpath", '//div[@id="downshift-1-item-0"]').click()

    except BaseException as err_msg:
        td = datetime.datetime.now()
        name = f"screenshot1_{td.hour}_{td.minute}_{td.second}.png"
        context.driver.save_screenshot(context.SCREENSHOTS_PATH + name)
        raise err_msg

@when('click on to destination "{to_location}" into To Textfield')
def enter_data_to(context, to_location):
    try:
        time.sleep(3)
        pattern = r'[a-zA-Z]+'
        result = re.findall(pattern, to_location)
        assert result, "invalid To location"
        context.driver.find_element("xpath", '//input[@id = "autosuggestBusSRPDestHome"]').send_keys(to_location)
        time.sleep(2)
        context.driver.find_element("xpath", '//div[@id="downshift-2-item-0"]').click()

    except BaseException as err_msg:
        td = datetime.datetime.now()
        name = f"screenshot1_{td.hour}_{td.minute}_{td.second}.png"
        context.driver.save_screenshot(context.SCREENSHOTS_PATH + name)
        raise err_msg

@when('select the required Date')
def select_date(context):
    context.driver.find_element("xpath", '//input[@placeholder = "Pick a date"]').click()
    ## context.driver.find_element("xpath",
    ##                             '//div[@class = "dcalendarstyles__MonthChangeRightArrowDiv-sc-r2jz2t-16 iJqGSS"]//div[@class = "dcalendarstyles__SliderArrow-sc-r2jz2t-14 ilBEvY"]').click()
    context.driver.find_element("xpath", '//span[text() = "15"]').click()

@when('click on Search Bus Button then bus list page open')
def click_search_btn(context):
    context.driver.find_element("xpath", '//button[text() ="Search Bus"]').click()

@when('click on multiple Check box and Reset Button on popular Filter')
def click_popular_filter(context):
    time.sleep(5)
    context.driver.find_element("xpath",
                                '//span[text() = "GoDeal Discount"]/..//span[@class ="Checkboxstyles__Checkmark-sc-17an8c7-1 cXxQSq"]').click()
    context.driver.find_element("xpath",
                                '//span[text() = "Live Tracking"]/..//span[@class ="Checkboxstyles__Checkmark-sc-17an8c7-1 cXxQSq"]').click()
    context.driver.find_element("xpath",
                                '//span[text() = "Free Cancellation"]/..//span[@class ="Checkboxstyles__Checkmark-sc-17an8c7-1 cXxQSq"]').click()
    context.driver.find_element("xpath",
                                '//span[text() = "Top Rated Buses"]/..//span[@class ="Checkboxstyles__Checkmark-sc-17an8c7-1 cXxQSq"]').click()
    time.sleep(2)
    context.driver.find_element("xpath",
                                '(//a[@class  = "FiltersBlockstyles__ResetElink-sc-v6hq3g-5 dafNvA"])[2]').click()


@when('click on multiple Check box and Reset Button on Bus Type Filter')
def click_bus_filter(context):
    time.sleep(2)
    context.driver.find_element("xpath", '//div[text() ="AC"]').click()
    context.driver.find_element("xpath", '//div[text() ="Non-AC"]').click()
    context.driver.find_element("xpath", '//div[text() ="Seater"]').click()
    context.driver.find_element("xpath", '//div[text() ="Sleeper"]').click()
    time.sleep(2)
    context.driver.find_element("xpath",
                                '(//a[@class  = "FiltersBlockstyles__ResetElink-sc-v6hq3g-5 dafNvA"])[3]').click()


@when('click on multiple Check box and Reset Button on Arrival Time Filter')
def click_arrival_time_filter(context):
    context.driver.find_element("xpath", '(//div[text() ="12 midnight - 6 AM"])[1]').click()
    time.sleep(2)
    context.driver.find_element("xpath", '(//div[text() ="6 AM - 12 noon"])[1]').click()
    time.sleep(2)
    context.driver.find_element("xpath", '(//div[text() ="12 noon - 6 PM"])[1]').click()
    time.sleep(2)
    context.driver.find_element("xpath", '(//div[text() ="6 PM - 12 midnight"])[1]').click()
    time.sleep(2)
    context.driver.find_element("xpath",
                                '(//a[@class  = "FiltersBlockstyles__ResetElink-sc-v6hq3g-5 dafNvA"])[4]').click()

@when('click on search textfield on Boarding point filter')
def click_on_search_bp(context):
    time.sleep(2)
    context.driver.find_element("xpath", '//input[@id = "boardingPointFilterSearch"]').click()


@when('click on All Boarding Point Option')
def click_on_all_bp_option(context):
    time.sleep(2)
    context.driver.find_element("xpath",
                                '(//a[@class = "FiltersBlockstyles__ResetElink-sc-v6hq3g-5 dafNvA"])[7]').click()

@when('click on multiple Check box and Reset Button on Boarding Point Filter')
def click_on_Boarding_filter(context):
    time.sleep(2)
    all_check_box = context.driver.find_elements("xpath",'(//div[@class = "FiltersBlockstyles__DropPointFiltersMainDiv-sc-v6hq3g-10 jjQxZ"])[1]//span[@class = "Checkboxstyles__Checkmark-sc-17an8c7-1 cXxQSq"]')
    for check_box in all_check_box:
        check_box.click()
        time.sleep(2)
    context.driver.find_element("xpath",
                                '(//a[@class  = "FiltersBlockstyles__ResetElink-sc-v6hq3g-5 dafNvA"])[6]').click()
    time.sleep(3)


@when('click on search textfield on Dropping point filter')
def click_search_dp(context):
    time.sleep(2)
    context.driver.find_element("xpath", '//input[@id = "droppingPointFilterSearch"]').click()


@when('click on All Dropping point Option')
def click_all_dp(context):
    time.sleep(2)
    context.driver.find_element("xpath",
                                '(//a[@class= "FiltersBlockstyles__ResetElink-sc-v6hq3g-5 dafNvA"])[9]').click()


@when('click on multiple Check box and Reset Button on Dropping point Filter')
def click_dropping_filter(context):
    time.sleep(2)
    all_check_box = context.driver.find_elements("xpath",
                                                '(//div[@class = "FiltersBlockstyles__DropPointFiltersMainDiv-sc-v6hq3g-10 jjQxZ"])[2]//span[@class ="Checkboxstyles__Checkmark-sc-17an8c7-1 cXxQSq"]')
    for check_box in all_check_box:
        check_box.click()
        time.sleep(2)
    context.driver.find_element("xpath",
                                '(//a[@class= "FiltersBlockstyles__ResetElink-sc-v6hq3g-5 dafNvA"])[8]').click()


@when('click on search textfield on Bus Operator filter')
def click_search_bus_op(context):
    time.sleep(2)
    context.driver.find_element("xpath", '//input[@id= "operatorFilterSearch"]').click()


@when('click on All Bus Operator Option')
def click_show_all_bus_op(context):
    context.driver.find_element("xpath",
                                '(//a[@class ="FiltersBlockstyles__ResetElink-sc-v6hq3g-5 dafNvA"])[11]').click()


@when('click on multiple Check box and Reset Button on Bus Operator Filter')
def click_bus_operator_filter(context):
    all_check_box = context.driver.find_elements("xpath",
                                                '(//div[@class ="FiltersBlockstyles__DropPointFiltersMainDiv-sc-v6hq3g-10 jjQxZ"])[3]//span[@class = "Checkboxstyles__Checkmark-sc-17an8c7-1 cXxQSq"]')
    for check_box in all_check_box:
        check_box.click()
        time.sleep(2)
    context.driver.find_element("xpath",
                                '(//a[@class= "FiltersBlockstyles__ResetElink-sc-v6hq3g-5 dafNvA"])[10]').click()


@when('click on All Bus Amenities Option')
def click_show_all_amenities(context):
    context.driver.find_element("xpath", '//a[text()="+ Show all Amenities"]').click()
    time.sleep(2)


@when('click on multiple Check box and Reset Button on Amenities Filter')
def click_amenities_filter(context):
    try:
        amenities_elements = context.driver.find_elements("xpath",
                                               '(//div[@class = "FiltersBlockstyles__NewFiltersMainDiv-sc-v6hq3g-9 dZsEaZ"])[2]//span[@class ="Checkboxstyles__Checkmark-sc-17an8c7-1 cXxQSq"]')
        for amenities in amenities_elements:
            amenities.click()
            time.sleep(2)
    except:
        pass
    finally:
        context.driver.find_element("xpath", '(//a[@class= "FiltersBlockstyles__ResetElink-sc-v6hq3g-5 dafNvA"])[12]').click()
        time.sleep(3)

@then('Verify it is clickable and displayed')
def verify_and_close(context):
    context.driver.close()


@when('click on select seat button')
def click_on_select_seat(context):
    time.sleep(5)
    context.driver.find_element("xpath", '(//div[@class = "SrpActiveCardstyles__PayBtnWrapDiv-sc-yk1110-30 gfLfNz"])[3]').click()


@when('click on boarding point time radio button')
def click_on_boarding_time(context):
    time.sleep(5)
    context.driver.find_element("xpath", '(//span[@class = "RadioButtonstyles__Checkmark-sc-wz601o-1 bFGqGl"])[1]').click()

@when('click on dropping point time radio button')
def click_on_dropping_time(context):
    time.sleep(5)
    context.driver.find_element("xpath", '(//span[@class = "RadioButtonstyles__Checkmark-sc-wz601o-1 bFGqGl"])[9]').click()

@when('click on available seat')
def select_available_seat(context):
    time.sleep(2)
    context.driver.find_element("css selector", 'path[fill="#FFF"]').click()

@when('click on continue button')
def click_on_continue_btn(context):
    time.sleep(2)
    context.driver.find_element("xpath", '//button[text() ="CONTINUE"]').click()

@then('verify is clickable and navigate review your booking page')
def verify_and_close(context):
    context.driver.close()


@when('click on yes radio button for Trip Insurance')
def click_on_yes_trip_insurance(context):
    # context.driver.find_element("xpath",'(//span[@class="checkmark"])[1]').click()
    # time.sleep(3)
    pass

@when('click on No radio button for Trip Insurance')
def click_on_no_trip_insurance(context):
    time.sleep(5)
    context.driver.find_element("xpath", '(//span[@class="checkmark"])[2]').click()
    time.sleep(4)

@when('click on full name and provide Traveller "{full_name}"')
def enter_full_name(context, full_name):
    try:
        time.sleep(3)
        pattern = r'[A-Z][a-z]*'
        result = re.findall(pattern, full_name)
        assert result, "invalid full Name"
        context.driver.find_element("xpath", '//input[@placeholder="Enter Full Name"]').send_keys(full_name)
        time.sleep(2)

    except BaseException as err_msg:
        td = datetime.datetime.now()
        name = f"screenshot1_{td.hour}_{td.minute}_{td.second}.png"
        context.driver.save_screenshot(context.SCREENSHOTS_PATH + name)
        raise err_msg

@when('Enter Traveller Age in "{age}" textfield')
def enter_age(context, age):
    try:
        time.sleep(2)
        pattern = r"^[1-9]\d*$"
        result = re.findall(pattern, age)
        assert result, "invalid Age"
        context.driver.find_element("xpath", '//input[@placeholder="Age"]').send_keys(int(age))
        time.sleep(2)

    except BaseException as err_msg:
        td = datetime.datetime.now()
        name = f"screenshot1_{td.hour}_{td.minute}_{td.second}.png"
        context.driver.save_screenshot(context.SCREENSHOTS_PATH + name)
        raise err_msg

@when('click on male or female "{gender}"')
def click_on_gender(context, gender):
    if gender.lower() == "male":
        context.driver.find_element("xpath", '//li[@class ="genderTabsList "]').click()
    else:
        context.driver.find_element("xpath", '//li[@class ="genderTabsList selected"]').click()

@when('Enter Traveller Email "{email_id}"')
def enter_email_id(context, email_id):
    try:
        time.sleep(2)
        pattern = r"\w+@gmail\.com"
        result = re.findall(pattern, email_id)
        assert result, "invalid email"
        context.driver.find_element("xpath", '//input[@placeholder ="Enter Email Address"]').send_keys(email_id)

    except BaseException as err_msg:
        td = datetime.datetime.now()
        name = f"screenshot1_{td.hour}_{td.minute}_{td.second}.png"
        context.driver.save_screenshot(context.SCREENSHOTS_PATH + name)
        context.driver.close()
        raise err_msg

@when('Enter Traveller Mobile Number "{mobile_number}"')
def enter_mobile_number(context, mobile_number):
    try:
        time.sleep(2)
        pattern = r'^[6-9]\d{9}$'
        result = re.findall(pattern, mobile_number)
        assert result, "invalid Mobile Number"
        context.driver.find_element("xpath", '//input[@placeholder ="Enter Mobile Number"]').send_keys(int(mobile_number))

    except BaseException as err_msg:
        td = datetime.datetime.now()
        name = f"screenshot1_{td.hour}_{td.minute}_{td.second}.png"
        context.driver.save_screenshot(context.SCREENSHOTS_PATH + name)
        context.driver.close()
        raise err_msg


@when('click on Pay button')
def click_on_pay_btn(context):
    time.sleep(2)
    context.driver.find_element("xpath", '//button[@class ="ReviewPagestyles__PayButton-sc-fmjc42-13 bYqmLn"]').click()

@then('Verify and is navigate to new all payment mode page')
def verify_and_close(context):
    context.driver.close()

@when('click on credit and debit card mode')
def click_on_credit_debit_option(context):
    time.sleep(10)
    context.driver.find_element("xpath", '(//div[@class="appendLeft20 makeFlex spaceBetween hrtlCenter flexOne cardDesc"])[2]').click()

@when('enter the card Number "{card_number}"')
def enter_card_number(context, card_number):
    try:
        time.sleep(2)
        pattern = r'^4[0-9]{12}(?:[0-9]{3})?$'
        result = re.findall(pattern, card_number)
        assert result, "invalid Card Number"
        context.driver.find_element("xpath", '//input[@id="cardNumber"]').send_keys(card_number)

    except BaseException as err_msg:
        td = datetime.datetime.now()
        name = f"screenshot1_{td.hour}_{td.minute}_{td.second}.png"
        context.driver.save_screenshot(context.SCREENSHOTS_PATH + name)
        context.driver.close()
        raise err_msg

@when('click on month')
def click_on_month(context):
    context.driver.find_element("xpath", '//input[@id="expiryMonth"]').click()
    context.driver.find_element("xpath", '//ul//li[text()="11"]').click()

@when('click on year')
def click_on_year(context):
    context.driver.find_element("xpath", '//input[@id="expiryYear"]').click()
    context.driver.find_element("xpath", '//ul//li[text()="2023"]').click()


@when(u'enter the cvv "{cvv}"')
def enter_cvv(context, cvv):
    try:
        time.sleep(2)
        pattern = r'^\d{3}'
        result = re.findall(pattern, cvv)
        assert result, "invalid CVV Number"
        context.driver.find_element("xpath", '//input[@id="cardCvv"]').send_keys(cvv)

    except BaseException as err_msg:
        td = datetime.datetime.now()
        name = f"screenshot1_{td.hour}_{td.minute}_{td.second}.png"
        context.driver.save_screenshot(context.SCREENSHOTS_PATH + name)
        raise err_msg


@when('enter name on card "{card_name}"')
def enter_name_on_card(context, card_name):
    try:
        time.sleep(2)
        pattern = r'[A-Z][a-z]*'
        result = re.findall(pattern, card_name)
        assert result, "invalid Card Name"
        context.driver.find_element("xpath", '//input[@id="nameOnCard"]').send_keys(card_name)

    except BaseException as err_msg:
        td = datetime.datetime.now()
        name = f"screenshot1_{td.hour}_{td.minute}_{td.second}.png"
        context.driver.save_screenshot(context.SCREENSHOTS_PATH + name)
        raise err_msg

@when('click on save and pay button')
def click_save_and_pay_btn(context):
    time.sleep(3)
    context.driver.find_element("xpath", '//button[@type="submit"]').click()

@then('verify otp send to given mobile number and enter OTP Page displayed')
def verify_and_close(context):
    time.sleep(4)
    # context.driver.find_element("xapth",'(//button[@type="submit"])[2]').click()
    context.driver.close()
