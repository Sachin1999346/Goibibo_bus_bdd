import datetime
import re
import time

from behave import *
from selenium import webdriver
SCREENSHOTS_PATH = r'C:\Users\Shree\PycharmProjects\BDD Project\Screenshots\\'

@given('open the browser and enter the valid url')
def enter_browser_link(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.goibibo.com/")
    context.driver.maximize_window()

@when('click on bus button')
def click_on_bus_btn(context):
    time.sleep(5)
    context.driver.find_element("xpath",'//a[text()="Bus"]').click()

@then('Verify bus page is displayed')
def bus_page_displayed(context):
    context.driver.close()

@when('Enter the From "{from_location}"')
def enter_data(context, from_location):
    try:
        time.sleep(4)
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

@when('Click on To Testfiled and Enter the Destination "{to_location}"')
def enter_data_to(context, to_location):
    try:
        time.sleep(4)
        pattern = r'[a-zA-Z]+'
        result = re.findall(pattern, to_location)
        assert result, "invalid To location"
        context.driver.find_element("xpath", '//input[@id = "autosuggestBusSRPDestHome"]').send_keys(to_location)
        time.sleep(3)
        context.driver.find_element("xpath", '//div[@id="downshift-2-item-0"]').click()

    except BaseException as err_msg:
        td = datetime.datetime.now()
        name = f"screenshot1_{td.hour}_{td.minute}_{td.second}.png"
        context.driver.save_screenshot(context.SCREENSHOTS_PATH + name)
        raise err_msg

@then('Verify is displayed')
def close_method(context):
    context.driver.close()

@when('User click on Today date Button')
def click_today_date(context):
    # context.driver.find_element("xpath",'(//span[@class ="active"])[1]').click()
    pass

@when('User click on Tomorrow date Button')
def click_tomorrow_date(context):
    context.driver.find_element("xpath", '//span[text() ="Tomorrow"]').click()

@then('Verify that is clickable')
def close_browser(context):
   context.driver.close()

@when('click on Travel Date')
def click_on_travel_date(context):
    context.driver.find_element("xpath",'//input[@placeholder = "Pick a date"]').click()

@when('click on next month Arrow button')
def click_on_next_arrow(context):
    # context.driver.find_element("xpath", '//div[@class = "dcalendarstyles__MonthChangeRightArrowDiv-sc-r2jz2t-16 iJqGSS"]//div[@class = "dcalendarstyles__SliderArrow-sc-r2jz2t-14 ilBEvY"]').click()
    pass
@when('select any today onward date')
def select_date(context):
    context.driver.find_element("xpath", '//span[text() = "15"]').click()

@then('Verify that is select and displayed')
def verify_and_close(context):
    context.driver.close()


@when('click on from textfield and enter source "{from_location}"')
def enter_data(context, from_location):
    try:
        time.sleep(4)
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

@when('enter the destination "{to_location}" into To Textfield')
def enter_data_to(context, to_location):
    try:
        time.sleep(4)
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

@when('select the date')
def select_date(context):
    context.driver.find_element("xpath", '//input[@placeholder = "Pick a date"]').click()
    # context.driver.find_element("xpath", '//div[@class = "dcalendarstyles__MonthChangeRightArrowDiv-sc-r2jz2t-16 iJqGSS"]//div[@class = "dcalendarstyles__SliderArrow-sc-r2jz2t-14 ilBEvY"]').click()
    context.driver.find_element("xpath", '//span[text() = "15"]').click()

@when('click on Search Bus button')
def click_search_btn(context):
    context.driver.find_element("xpath",'//button[text() ="Search Bus"]').click()

@then('Verify it navigate to next page')
def verify_and_close(context):
    context.driver.close()

