# import pytest
# from selenium.webdriver.common.by import By
# from utils.actions import login
# from utils.assertions.elements import assert_text
# from utils.constants import LOGIN_TEST_SETS

# @pytest.mark.parametrize(
#         "username, password, selector, expected_text", 
#         LOGIN_TEST_SETS.invalid_inputs
#     )
# def test_login_failed(driver, username, password, selector, expected_text):
#     login(username, password, driver)
#     assert_text(driver, By.CSS_SELECTOR, selector, expected_text, context="Login inválido")