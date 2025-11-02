
#! -- Deprecado -- 
# TODO  Validar para eliminar
# TODO Eliminar archivo 

# import pytest
# from selenium.webdriver.remote.webdriver import WebDriver
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException, WebDriverException
# from utils.actions import wait_for_element
# 
# def contains_element(selector: str, by: By, driver: WebDriver) -> bool:
    # try:
        # driver.find_element(by, selector)
        # return True
    # except NoSuchElementException:
        # return False
# 
# def page_title_is(text, driver: WebDriver) -> bool:
    # try:
        # return text in driver.title 
    # except WebDriverException:
        # return False
# 
# def contains_text(by: By, selector: str, expected_text: str, driver: WebDriver) -> bool:
    # try:
        # element = driver.find_element(by, selector)
        # return expected_text in element.text
    # except NoSuchElementException:
        # return False
    # 
# def contains_texts(elements: list[tuple], driver: WebDriver) -> bool:
    # results = []
    # for by, selector, text in elements:
        # result = contains_text(by, selector, text, driver)
        # if not result:
            # return False
    # return all(results)
# 
# 