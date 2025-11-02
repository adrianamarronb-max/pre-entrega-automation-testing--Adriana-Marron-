import pytest
from utils.actions import login, click_element
from utils.assertions.navigation import assert_current_url_contains
from utils.assertions.elements import assert_elements, assert_text
from utils.constants import(
    VALID_USER,
    VALID_PASS,
    PRODUCT_URL,
    CART_URL,
    CART_ELEMENTS,
    BY_CLASS,
    CLASS_STORE_TITLE,
    TEXTS,
    BTN_ADD_TO_CART,
    BTN_CART_LINK
    )

@pytest.mark.smoke
def test_cart_flow(driver):
    """
    🧪 Verifica el flujo principal hasta el carrito de compras.

    Flujo:
      1️⃣ Login exitoso.
      2️⃣ Acceso al catálogo.
      3️⃣ Agregar primer producto al carrito.
      4️⃣ Acceso al carrito.
      5️⃣ Validar estructura y contenido del carrito.
    """
    login(VALID_USER, VALID_PASS, driver)
    assert_current_url_contains(driver, PRODUCT_URL, context="Catálogo post-login")
    assert_text(
        driver,
        BY_CLASS,
        CLASS_STORE_TITLE,
        TEXTS["inventory"]["title"],
        context="Catálogo"
    )
    click_element(driver, BY_CLASS, BTN_ADD_TO_CART)
    click_element(driver, BY_CLASS, BTN_CART_LINK)
    assert_current_url_contains(driver, CART_URL, context="Carrito")
    assert_text(
        driver,
        BY_CLASS,
        CLASS_STORE_TITLE,
        TEXTS["cart"]["title"],
        context="Carrito"
    )

    assert_elements(
        driver,
        CART_ELEMENTS,
        context="Carrito - Estructura principal"
    )