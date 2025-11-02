import pytest
from utils.actions import login
from utils.assertions.navigation import assert_current_url_contains
from utils.assertions.elements import assert_text
from utils.constants import( 
    LOGIN_TEST_DATA,
    PRODUCT_URL,
    CLASS_STORE_TITLE,
    TEXTS,
    TEXTS,
    BY_CSS,
    BY_CLASS,
)

@pytest.mark.parametrize(
    "username, password, should_succeed, selector, expected_message, mark_type",
    LOGIN_TEST_DATA,
    ids=[
        "Empty user and pass",
        "User without password",
        "Invalid user and pass",
        "Locked out user (error)",
        "Standard user (success)",
        "Problem user (success but UI issues)",
        "Performance glitch user (slow login)",
        "Error user (backend issue)",
        "Visual user (layout validation)",
    ],
)
def test_login_flow(
    driver,
    username,
    password,
    should_succeed,
    selector,
    expected_message,
    mark_type
):
    """
    🔁 Test unificado de login:
    Cubre casos negativos, positivos y de usuarios restringidos.
    """
    login(username, password, driver)
    if should_succeed:
        assert_current_url_contains(driver, PRODUCT_URL, context=f"Login {username} ({mark_type})")
        assert_text(
            driver,
            BY_CLASS,
            CLASS_STORE_TITLE,
            TEXTS["inventory"]["title"],
            context=f"Login - {username}",
        )
    else:
        assert_text(
            driver,
            BY_CSS,
            selector,
            expected_message,
            context=f"Fail log in ({username or 'empty'})",
        )