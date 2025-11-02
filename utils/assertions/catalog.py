from selenium.webdriver.common.by import By
from utils.assertions.elements import assert_elements
from utils.constants import CATALOG_ELEMENTS, CART_ELEMENTS

def assert_catalog_loaded(driver):
    """
    ✅ Verifica que la página del catálogo haya cargado correctamente.

    Revisa que los elementos esenciales del catálogo estén visibles:
    - Lista de productos
    - Nombres y precios
    - Botones "Add to cart"

    Args:
        driver (WebDriver): Instancia activa del navegador Selenium.

    Raises:
        AssertionError: Si algún elemento esperado no está visible o falla la carga.
    """
    assert_elements(driver, CATALOG_ELEMENTS, context="Catálogo de productos")

