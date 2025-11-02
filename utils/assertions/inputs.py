import re
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

from utils.actions import wait_for_element


def assert_input_value(
    driver: WebDriver,
    by: By,
    selector: str,
    expected_value: str,
    context: str = "page"
):
    """
    ✅ Verifica que un campo input contenga un valor específico después de ser llenado.

    Args:
        driver (WebDriver): Instancia activa del navegador.
        by (By): Tipo de localizador (By.ID, By.NAME, etc.).
        selector (str): Selector del campo.
        expected_value (str): Valor esperado dentro del input.
        context (str, optional): Descripción del área o pantalla actual.

    Raises:
        AssertionError: Si el valor del input no coincide con el esperado.
    """
    element = wait_for_element(driver, by, selector)
    actual_value = element.get_attribute("value").strip()
    assert expected_value == actual_value, (
        f"Valor esperado '{expected_value}' no coincide con el actual '{actual_value}' "
        f"en {context} (selector: '{selector}')."
    )

def assert_input_accepts(
    driver: WebDriver,
    by: By,
    selector: str,
    test_value: str,
    allowed_pattern: str,
    context: str = "page"
):
    """
    ✅ Verifica que un campo input acepte un tipo de valor específico.

    Args:
        driver (WebDriver): Instancia activa del navegador.
        by (By): Tipo de localizador (By.ID, By.NAME, etc.).
        selector (str): Selector del campo.
        test_value (str): Valor que se intenta ingresar en el campo.
        allowed_pattern (str): Expresión regular del formato permitido.
            Ejemplos:
                r'^[a-zA-Z]+$' → Solo letras
                r'^\\d+$' → Solo números
                r'^[a-zA-Z0-9]+$' → Alfanuméricos
        context (str, optional): Descripción del área o pantalla actual.

    Raises:
        AssertionError: Si el campo no acepta el valor o no cumple con el patrón permitido.
    """
    element = wait_for_element(driver, by, selector)
    element.clear()
    element.send_keys(test_value)

    actual_value = element.get_attribute("value").strip()
    matches_pattern = bool(re.match(allowed_pattern, actual_value))

    assert matches_pattern, (
        f"El valor '{actual_value}' ingresado no cumple con el patrón permitido "
        f"({allowed_pattern}) en {context} (selector: '{selector}')."
    )

def assert_input_type(
    driver: WebDriver,
    by: By,
    selector: str,
    expected_type: str,
    context: str = "page"
):
    """
    🔒 Verifica que un campo input sea del tipo esperado (por ejemplo, 'password', 'text', 'email').

    Args:
        driver (WebDriver): Instancia activa del navegador Selenium.
        by (By): Tipo de localizador (By.ID, By.NAME, etc.).
        selector (str): Selector del campo input.
        expected_type (str): Tipo esperado del input ('text', 'password', etc.).
        context (str, optional): Descripción del área o pantalla actual.

    Raises:
        AssertionError: Si el campo no tiene el tipo esperado.
    """
    element = wait_for_element(driver, by, selector)
    actual_type = element.get_attribute("type").strip().lower()

    assert actual_type == expected_type.lower(), (
        f"❌ El campo '{selector}' tiene tipo '{actual_type}' en lugar de '{expected_type}' "
        f"en {context}."
    )