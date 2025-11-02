import pytest
from utils.assertions.elements import assert_element, assert_elements, assert_text
from utils.assertions.navigation import assert_current_url_contains
from utils.actions import open_loging_page, wait_for_element

from utils.constants import (
  BASE_URL, 
  LOGIN_ELEMENTS, 
  BY_CLASS,
  CLASS_LOGIN_LOGO,
  LANDING_MESSAGE, 
  LOGIN_ELEMENTS, 
  CLASS_STORE_TITLE)

@pytest.mark.smoke
def test_access(driver):
    """
    🧪 Verifica el acceso inicial a la página de login.
    Valida:
      - Que se abra la página de SauceDemo correctamente.
      - Que los elementos principales de la pantalla estén visibles.
      - Que los textos esperados estén presentes.
    """
    open_loging_page(driver)
    assert_current_url_contains(driver, BASE_URL, context="Login")
    assert_elements(
      driver, 
      LOGIN_ELEMENTS, 
      context="Login - Estructura principal", 
      exact=False)
    assert_text(
      driver, 
      BY_CLASS, 
      CLASS_LOGIN_LOGO,
      LANDING_MESSAGE,
      context="Login title")
