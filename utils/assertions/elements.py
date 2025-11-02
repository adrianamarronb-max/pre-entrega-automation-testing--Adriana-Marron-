from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from utils.actions import wait_for_element


def assert_element(
        driver: WebDriver,
        by: By,
        selector: str,
        context: str = "page"
        ):
    
    """
    ✅ Verifica que un elemento sea visible en el DOM.

    Args:
        driver (WebDriver): Instancia activa del navegador.
        by (By): Tipo de selector.
        selector (str): Localizador del elemento.
        context (str, optional): Descripción del área actual.

    Raises:
        AssertionError: Si el elemento no se encuentra visible.
    """
    try:
        wait_for_element(driver, by, selector)
    except (NoSuchElementException, TimeoutException):
        assert False, f"Element '{selector}' not found or not visible in {context}"

def assert_text(
        driver: WebDriver, 
        by: By, 
        selector: str,  
        expected_text: str, 
        context: str = "page"
    ):
    """
    ✅ Verifica que un elemento visible contenga exactamente el texto esperado.

    Args:
        driver (WebDriver): Instancia activa del navegador Selenium.
        by (By): Tipo de localizador (By.ID, By.CSS_SELECTOR, etc.).
        selector (str): Valor del localizador del elemento.
        expected_text (str): Texto exacto que se espera encontrar dentro del elemento.
        context (str, optional): Descripción del área o pantalla actual (por ejemplo: "Login").

    Raises:
        AssertionError:
            - Si el elemento no existe o no es visible.
            - Si el texto no coincide exactamente con el esperado.
    """
    try:
        element = wait_for_element(driver, by, selector)
        actual = element.text.strip()
        assert expected_text == actual, (
            f"In {context}: expected text: \n'{expected_text}'\n"
            f"but it got:\n'{actual}'\n"
            f"Selector used: '{selector}'"
            )
    except (NoSuchElementException, TimeoutException):
        assert False, f"Element '{selector}' not found in {context}"

def assert_elements(
    driver: WebDriver,
    elements: list[tuple],
    context: str = "page",
    exact: bool = False
    ):
    """
    🧩 Valida que cada selector contenga o coincida exactamente con el texto esperado.
    Si el texto está vacío, valida solo la existencia del elemento.

    Args:
        driver (WebDriver): Instancia activa del navegador Selenium.
        elements (list[tuple]): Lista de tuplas (By, selector, expected_text)
        context (str, optional): Descripción del área o pantalla actual.
        exact (bool, optional): Si es True, exige coincidencia exacta.

    Raises:
        AssertionError:
            - Si el elemento no se encuentra o no es visible.
            - Si el texto esperado no coincide o no está contenido.
    """
    for by, selector, expected_text in elements:
        try:
            element = wait_for_element(driver, by, selector)
            actual = element.text.strip()
            if expected_text:
                if exact:
                    assert expected_text == actual, (
                        f"[{context}] Texto exacto no coincide.\n"
                            f"Expected:\n'{expected_text}'\n"
                            f"Got:\n'{actual}'\n"
                            f"Selector: {selector}"
                        )
                else: 
                    assert expected_text in actual, (
                        f"[{context}] Text '{expected_text}' not found in '{selector}'.\n"
                        f"Actual text:\n{actual}"
                    )
            else:
                assert element.is_displayed(), (
                    f"[{context}] The element '{selector}' is not visible."
                )

        except (NoSuchElementException, TimeoutException):
            raise AssertionError(f"[{context}] Element '{selector}' not found or not visible.")
