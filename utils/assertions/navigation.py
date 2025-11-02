from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

from utils.actions import wait_for_element


def assert_current_url_contains(
    driver: WebDriver,
    expected_fragment: str,
    context: str = "page"
):
    """
    🌐 Verifica que la URL actual contenga una ruta o fragmento esperado.

    Args:
        driver (WebDriver): Instancia activa del navegador.
        expected_fragment (str): Parte esperada de la URL (por ejemplo '/inventory.html').
        context (str, optional): Descripción del área o pantalla actual.

    Raises:
        AssertionError: Si la URL actual no contiene el fragmento esperado.
    """
    current_url = driver.current_url
    assert expected_fragment in current_url, (
        f"En {context}: se esperaba URL con '{expected_fragment}', "
        f"pero se obtuvo '{current_url}'."
    )

def assert_clickable(
    driver: WebDriver,
    by: By,
    selector: str,
    context: str = "page"
):
    """
    ✅ Verifica que un elemento sea clickeable (visible y habilitado).

    Usa la misma lógica de sincronización que `click_element()`,
    pero sin realizar el clic (solo valida que sea posible).

    Args:
        driver (WebDriver): Instancia activa del navegador.
        by (By): Tipo de localizador.
        selector (str): Selector del elemento.
        context (str, optional): Descripción del área o pantalla actual.

    Raises:
        AssertionError: Si el elemento no es visible o no está habilitado.
    """
    element = wait_for_element(driver, by, selector)
    assert element.is_displayed() and element.is_enabled(), (
        f"Elemento '{selector}' no clickeable o deshabilitado en {context}."
    )


def assert_focusable(
    driver: WebDriver,
    by: By,
    selector: str,
    context: str = "page"
):
    """
    ✅ Verifica que un elemento pueda recibir el foco sin generar interacción visible.

    Args:
        driver (WebDriver): Instancia activa del navegador.
        by (By): Tipo de localizador.
        selector (str): Selector del elemento.
        context (str, optional): Descripción del área o pantalla actual.

    Raises:
        AssertionError: Si el elemento no puede recibir foco.
    """
    element = wait_for_element(driver, by, selector)
    assert element.is_displayed(), (
        f"El elemento '{selector}' no está visible en {context}."
    )
    assert element.is_enabled(), (
        f"El elemento '{selector}' está deshabilitado en {context}."
    )

