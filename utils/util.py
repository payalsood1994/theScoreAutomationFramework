
import datetime
import os

import subprocess
import subprocess as sub
import time
import urllib.error
import urllib.parse
import urllib.request
from configparser import RawConfigParser
from utils.locators.android_locators import *
from random import randint

import requests
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import utils.util

def __init__(self, driver):
    super().__init__()
    self.driver = driver
    self.common_locator = CommonLocator


def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")

def getNumbersFromString(str):
    return [int(s) for s in str.split() if s.isdigit()]


def create_dir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)


def getsize(uri):
    file = urllib.request.urlopen(uri)
    size = file.headers.get("content-length")
    file.close()
    return int(size)


def try_except_screenshot(driver, path, title, __name__, language):
    try:
        driver.save_screenshot(path + title % (__name__, language))
    except Exception:
        pass


def is_element_present_by_id(driver, name):
    """
    Checks if the given element is present on the site.
    :param driver: the webdriver
    :param name: the id of the desired element
    :return: the boolean representing whether the element is present
    """
    try:
        driver.find_element_by_id(name)
        return True
    except NoSuchElementException:
        return False


def is_element_present_by_css(driver, name):
    """
    Checks if the given element is present on the site.
    :param driver: the webdriver
    :param name: the id of the desired element
    :return: the boolean representing whether the element is present
    """
    try:
        driver.find_element_by_css_selector(name)
        return True
    except NoSuchElementException:
        return False


def is_element_present_by_xpath(driver, name):
    """
    Checks if the given element is present on the site.
    :param driver: the webdriver
    :param name: the id of the desired element
    :return: the boolean representing whether the element is present
    """
    try:
        driver.find_element_by_xpath(name)
        return True
    except NoSuchElementException:
        return False


def get_locator_by_string(locator_with_type):
    """
    In locator_with_type we're passing locator in string format with type:id, xpath, accessibility_id, class. This
    method splits up string and based on type of locator in the string it returns MobileBy locator
    :param locator_with_type:
    :return:
    """
    # For debugging
    # print("!!!!!" + str(locator_with_type))
    print(locator_with_type)
    splitted_locator = locator_with_type.split(":", 1)
    print(splitted_locator)
    by_type = splitted_locator[0]
    locator = splitted_locator[1]

    if by_type == "xpath":
        return MobileBy.XPATH, locator
    elif by_type == "css":
        return MobileBy.CSS_SELECTOR, locator
    elif by_type == "id":
        return MobileBy.ID, locator
    elif by_type == "accessibility_id":
        return MobileBy.ACCESSIBILITY_ID, locator
    elif by_type == "class":
        return MobileBy.CLASS_NAME, locator
    else:
        raise Exception("Cannot get type of locator. Locator {locator_with_type}")


def wait_for_element_present(driver, by_locator: str, timeout_in_seconds):
    """
    Wait for element to present within timeout_in_seconds
    :param driver:
    :param by_locator: locator of desired element
    :param timeout_in_seconds: timeout
    :return: WebElement
    """
    # Initially locator presented as dictionary (Android or iOS). Select either its Android or iOS locator
    #locator_for_platform = select_locator_for_platform(by_locator)

    # Return the part of the string that represents the actual locator
    by = get_locator_by_string(by_locator)
    try:
        return WebDriverWait(driver, timeout_in_seconds).until(
            EC.presence_of_element_located(by), " : ".join(by)
        )
    except TimeoutException:
        raise ValueError("Element %s not found" % str(by))


def wait_for_many_elements_present(driver, by_locator: str, timeout_in_seconds):
    """
    Wait for list of elements to present within timeout_in_seconds
    :param driver:
    :param by_locator: locator of desired elements
    :param timeout_in_seconds: timeout
    :return: list of WebElement
    """
    # Return the part of the string that represents the actual locator
    by = get_locator_by_string(by_locator)
    try:
        return WebDriverWait(driver, timeout_in_seconds).until(
            EC.presence_of_all_elements_located(by), " : ".join(by)
        )
    except TimeoutException:
        raise ValueError("Element %s not found" % str(by))


def wait_for_element_be_visible(driver, by_locator: str, timeout_in_seconds):
    """
    Wait for element to be visible within timeout_in_seconds
    :param driver:
    :param by_locator: locator of desired element
    :param timeout_in_seconds: timeout
    :return: WebElement
    """
    by = get_locator_by_string(by_locator)
    try:
        return WebDriverWait(driver, timeout_in_seconds).until(
            EC.visibility_of_element_located(by), " : ".join(by)
        )
    except TimeoutException:
        raise ValueError("Element %s is not visible" % by_locator[1])


def wait_for_element_be_clickable(driver, by_locator: str, timeout_in_seconds):
    """
    Wait for element to be clickable within timeout_in_seconds
    :param driver:
    :param by_locator: locator of desired element
    :param timeout_in_seconds: timeout
    :return: WebElement
    """
    by = get_locator_by_string(by_locator)
    try:
        return WebDriverWait(driver, timeout_in_seconds).until(
            EC.element_to_be_clickable(by), " : ".join(by)
        )
    except TimeoutException:
        raise ValueError("Element %s is not clickable" % by_locator[1])


def wait_for_element_and_click(driver, by_locator: str, timeout_in_seconds):
    """
    Wait for element to be present within timeout_in_seconds and click
    :param driver:
    :param by_locator: locator of desired element
    :param timeout_in_seconds: timeout
    :return:
    """
    element = wait_for_element_present(driver, by_locator, timeout_in_seconds)
    try:
        element.click()
    except TimeoutException:
        raise ValueError("Driver could not click on the element: %s" % by_locator[1])


def wait_for_element_and_send_keys(driver, by_locator: str, keys, timeout_in_seconds):
    """
    Wait for element to be present within timeout_in_seconds and send keys
    :param driver:
    :param by_locator: locator of desired element
    :param keys: keys to be sent to text input
    :param timeout_in_seconds: timeout
    :return:
    """
    element = wait_for_element_present(driver, by_locator, timeout_in_seconds)
    try:
        element.send_keys(keys)
    except TimeoutException:
        raise ValueError(
            "Driver could not send keys to the element: %s" % by_locator[1]
        )


def get_text_from_element(driver, by_locator):
    """
    Get text attribute from WebElement
    :param driver:
    :param by_locator: locator of desired element
    :return:
    """
    element_text = wait_for_element_present(driver, by_locator, 5).text
    print(element_text)
    return element_text


def get_list_of_elements(driver, by_locator):
    """
    Get list of elements
    :param driver:
    :param by_locator: locator of desired element
    :return:
    """
    # locator = select_locator_for_platform(by_locator)
    elements = wait_for_many_elements_present(driver, by_locator, 15)
    return elements


""" SWipes and scrolls """


def tap_by_coordinates(driver, x, y):
    """
    Tap by [x,y] coordinates using Touch Action
    :param driver:
    :param x:
    :param y:
    :return:
    """
    touch = TouchAction(driver)
    size = driver.get_window_size()
    x1 = int(size["width"] * x)
    y1 = int(size["height"] * y)
    touch.tap(None, x1, y1, 1).perform()


def is_element_present(driver, element, timeout):
    """
    Method to verify is element presents or not
    :param driver:
    :param element: locator of desired element
    :param timeout: how long wait for element to display
    :return: boolean
    """

    # Initially locator presented as dictionary (Android or iOS). Select either its Android or iOS locator
    #locator_for_platform = select_locator_for_platform(element)
    # Return the part of the string that represents the actual locator
    by = get_locator_by_string(element)
    try:
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(by), " : ".join(by)
        )
        return True
    except TimeoutException:
        return False


def is_element_clickable(driver, element, timeout):
    """
    Method to verify is element clickable or not
    :param driver:
    :param element: locator of desired element
    :param timeout: how long wait for element to display
    :return: boolean
    """
    # Return the part of the string that represents the actual locator
    by = get_locator_by_string(element)
    try:
        WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(by), " : ".join(by)
        )
        return True
    except TimeoutException:
        return False


def soft_assert_equals(fails, x, y, assertion_error):
    """
    Function for soft assert equals. Allows to append assertion errors in the end of the test
    :param fails: Array where storing assertion errors
    :param x: Parameter x
    :param y: Parameter y
    :param assertion_error: Text of assertion error
    :return: assertion errors
    """
    try:
        assert x == y, assertion_error % (x, y)
    except AssertionError as e:
        fails.append(e)


def soft_assert_equals_three_params(fails, x, y, z, assertion_error):
    """
    Function for soft assert equals. Allows to append assertion errors in the end of the test
    :param fails: Array where storing assertion errors
    :param x: Parameter x
    :param y: Parameter y
    :param z: Parameter z
    :param assertion_error: Text of assertion error
    :return: assertion errors
    """
    try:
        assert x == y == z, assertion_error % (x, y, z)
    except AssertionError as e:
        fails.append(e)


def verify_element_displayed_or_throw_error(driver, locator, element_name: str):
    """
    Verify element found on the screen or throw the error message
    :param driver:
    :param locator: WebElement
    :param element_name: str
    """
    if not is_element_present(driver, locator, 10):
        raise ValueError(element_name + " missing")
    # else:
    #     print(element_name+" found")


def dismiss_model(driver):
    """
    Dismiss the model if appears
    :return:
    """
    if is_element_present(driver, CommonLocator.DISMISS_MODEL, 10):
      wait_for_element_and_click(driver, CommonLocator.DISMISS_MODEL, 10)





