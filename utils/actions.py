from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.constants import TIMEOUT
from utils.constants import( 
    BASE_URL,
    PRODUCT_URL,
    ID_USERNAME, 
    ID_PASSWORD, 
    ID_LOGIN_BUTTON,
    VALID_USER,
    VALID_PASS
    )

def open_loging_page(driver: WebDriver):
    """
    🌐 Abre la página de login de la aplicación.

    Args:
        driver (WebDriver): Instancia activa del navegador Selenium.

    Raises:
        AssertionError: Si la página no carga correctamente.
    """
    driver.get(BASE_URL)

def login(user: str, password: str, driver: WebDriver):
    """
    🔐 Realiza el flujo de login con las credenciales especificadas.

    Args:
        user (str): Nombre de usuario a ingresar.
        password (str): Contraseña correspondiente.
        driver (WebDriver): Instancia activa del navegador Selenium.

    Description:
        1. Abre la página de login.
        2. Completa los campos de usuario y contraseña.
        3. Hace clic en el botón de login.
    """
    driver.get(BASE_URL)

    fill_field(driver, By.ID, ID_USERNAME, user)
    fill_field(driver, By.ID, ID_PASSWORD, password)
    click_element(driver, By.ID, ID_LOGIN_BUTTON)

def wait_for_element(
        driver: WebDriver,
        by: By,
        selector: str,
        timeout: int = TIMEOUT
    ):
    """
    🕒 Espera hasta que un elemento sea visible en el DOM y lo devuelve.

    Args:
        driver (WebDriver): Instancia activa del navegador.
        by (By): Tipo de localizador (By.ID, By.CLASS_NAME, etc.).
        selector (str): Valor del localizador (por ejemplo '#login-button').
        timeout (int, optional): Tiempo máximo de espera (en segundos).

    Returns:
        WebElement: El elemento localizado y visible en pantalla.

    Raises:
        TimeoutException: Si el elemento no aparece dentro del tiempo límite.
    """
    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.visibility_of_element_located((by, selector)))

def fill_field(
        driver: WebDriver, 
        by: By, 
        selector: str, 
        text: str):
    """
    ⌨️ Completa un campo de texto en la página.

    Esta función espera a que el campo esté visible, opcionalmente lo limpia, y luego escribe el valor.
    Se usa comúnmente para ingresar usuario, contraseña, o realizar búsquedas.

    Args:
        driver (WebDriver): Instancia activa del navegador Selenium.
        by (By): Tipo de localizador (By.ID, By.NAME, etc.).
        selector (str): Valor del localizador del campo (por ejemplo, '#user-name').
        value (str): Texto que se desea escribir en el campo.
        clear (bool, optional): Si es True, limpia el campo antes de escribir. Por defecto, True.
        timeout (int, optional): Tiempo máximo de espera para que el campo sea visible. Por defecto, 5.

    Raises:
        AssertionError: Si el campo no se encuentra o no se puede completar.
    """
    element = wait_for_element(driver, by, selector)
    element.clear()
    element.send_keys(text)
    
def click_element(driver: WebDriver, by: By, selector: str):
    """
    🖱️ Realiza clic en un elemento visible de la página.

    Esta función utiliza `wait_for_element()` para asegurarse de que el elemento esté visible
    antes de hacer clic. Si no se encuentra o no es clickeable dentro del tiempo establecido,
    lanza una excepción.

    Args:
        driver (WebDriver): Instancia activa del navegador Selenium.
        by (By): Tipo de localizador (By.ID, By.CSS_SELECTOR, etc.).
        selector (str): Valor del localizador del elemento (por ejemplo, '#login-button').
        timeout (int, optional): Tiempo máximo de espera en segundos. Por defecto, 5.

    Raises:
        AssertionError: Si el elemento no se encuentra o no se puede clicar.
    """
    wait = WebDriverWait(driver, 5)
    element = wait.until(EC.element_to_be_clickable((by, selector)))
    element.click()

def go_to_catalog(driver):
    """
    🛒 Realiza el login y verifica la navegación al catálogo.
    """
    login(VALID_USER, VALID_PASS, driver)


def verify_product_exists(driver):
    """
    🔍 Verifica si existe al menos un producto visible en el catálogo.

    Args:
        driver (WebDriver): Instancia activa del navegador Selenium.

    Returns:
        bool: True si hay al menos un producto visible, False en caso contrario.
    """
    try:
        wait_for_element(driver, By.CLASS_NAME, "inventory_item")
        return True
    except Exception:
        return False