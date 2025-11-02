import pytest
from utils.actions import login, wait_for_element, click_element
from utils.assertions.navigation import assert_current_url_contains
from utils.assertions.elements import assert_text, assert_elements
from utils.assertions.catalog import assert_catalog_loaded
from utils.constants import (
    BASE_URL,
    PRODUCT_URL,
    CLASS_STORE_TITLE,
    BY_CLASS,
    BY_CSS,
    BY_ID,
    VALID_USER,
    VALID_PASS,
    TEXTS,
    CATALOG_ELEMENTS,
)

@pytest.mark.smoke
def test_catalog_access(driver):
    """
    🧪 Verifica el acceso al catálogo de productos luego del login.
    Valida:
      - Que el login sea exitoso.
      - Que el título "Products" esté visible.
      - Que los elementos de producto estén presentes.
    """
    login(VALID_USER, VALID_PASS, driver)
    assert_current_url_contains(driver, PRODUCT_URL, context="Catálogo")
    assert_text(
        driver,
        BY_CLASS,
        CLASS_STORE_TITLE,
        TEXTS["inventory"]["title"],
        context="Catálogo"
        )
    
    assert_elements(
        driver,
        CATALOG_ELEMENTS,
        context="Catálogo - Productos listados"
    )

@pytest.mark.smoke
def test_catalog_flow(driver):
    """
    🧪 Test de flujo del catálogo:
    1️⃣ Login con usuario válido.
    2️⃣ Validar carga del catálogo.
    3️⃣ Agregar producto al carrito.
    """
    login(VALID_USER, VALID_PASS, driver)
    assert_catalog_loaded(driver)

    # Agregar producto al carrito
    click_element(driver, BY_CLASS, "btn_inventory")