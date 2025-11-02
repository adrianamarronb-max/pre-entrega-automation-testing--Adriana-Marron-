from selenium.webdriver.common.by import By
from utils.assertions.elements import assert_elements
from utils.constants import CART_ELEMENTS

def assert_cart_loaded(driver):
    """
    🧾 Verifica que la página del carrito de compras se haya cargado correctamente.

    Comprueba:
    - Que el listado de productos del carrito esté visible.
    - Que las columnas de cantidad y descripción aparezcan.
    - Que no falten los elementos básicos de estructura.

    Args:
        driver (WebDriver): Instancia activa del navegador Selenium.

    Raises:
        AssertionError: Si algún elemento esperado no está visible o no contiene el texto esperado.
    """
    assert_elements(driver, CART_ELEMENTS, context="Carrito de compras")