
"""
* -- constants.py --
-------------
📘 Contiene todos los datos estáticos usados en los tests automatizados:
- URLs
- Selectores
- Textos esperados
- Credenciales
- Datos de prueba parametrizados
- Estructuras de elementos por pantalla (para asserts de UI)
"""
from selenium.webdriver.common.by import By

# ============================================================
# 🌐 URLs
# ============================================================
BASE_URL: str = "https://www.saucedemo.com"
PRODUCT_URL: str = f"{BASE_URL}/inventory.html"

# ============================================================
# 🧭 Selectores (By y valores)
# ============================================================
BY_ID = By.ID
BY_CLASS = By.CLASS_NAME
BY_XPATH = By.XPATH
BY_CSS = By.CSS_SELECTOR
BY_TAG = By.TAG_NAME

# Identificadores de elementos principales
ID_USERNAME = "user-name"
ID_PASSWORD = "password"
ID_LOGIN_BUTTON = "login-button"
ID_LOGIN_CREDENTIALS = "login_credentials"

CLASS_LOGIN_LOGO = "login_logo"
CLASS_LOGIN_PASSWORD = "login_password"
CLASS_STORE_TITLE = "title"

CSS_ERROR_MESSAGE = "[data-test='error']"
CSS_ERROR_ICON_USER = "#login_button_container > div > form > div:nth-child(1) > svg"
CSS_ERROR_ICON_PASS = "#login_button_container > div > form > div:nth-child(2) > svg"

# ============================================================
# 🔐 Selectores de Login
# ============================================================
ID_USERNAME = "user-name"
ID_PASSWORD = "password"
ID_LOGIN_BUTTON = "login-button"
ID_LOGIN_CREDENTIALS = "login_credentials"

CLASS_LOGIN_LOGO = "login_logo"
CLASS_STORE_TITLE = "title"

CSS_ERROR_MESSAGE = "[data-test='error']"
CSS_ERROR_ICON_USER = "#login_button_container > div > form > div:nth-child(1) > svg"
CSS_ERROR_ICON_PASS = "#login_button_container > div > form > div:nth-child(2) > svg"

# ============================================================
# 💬 Textos esperados en la página de Login
# ============================================================
LANDING_MESSAGE = "Swag Labs"

TEXTS = {
    "login": {
        # Mensajes exactos según comportamiento de la app
        "error_empty_username": "Epic sadface: Username is required",
        "error_empty_password": "Epic sadface: Password is required",
        "error_invalid": "Epic sadface: Username and password do not match any user in this service",
        "error_locked": "Epic sadface: Sorry, this user has been locked out.",
    },
    "inventory": {
        "title": "Products"
    }
}

LOGIN_ELEMENTS = [
    # 🧠 Bloque de credenciales de usuarios
    (By.ID, ID_LOGIN_CREDENTIALS, "Accepted usernames are:"),
    (By.ID, ID_LOGIN_CREDENTIALS, "standard_user"),
    (By.ID, ID_LOGIN_CREDENTIALS, "locked_out_user"),
    (By.ID, ID_LOGIN_CREDENTIALS, "problem_user"),
    (By.ID, ID_LOGIN_CREDENTIALS, "performance_glitch_user"),
    (By.ID, ID_LOGIN_CREDENTIALS, "error_user"),
    (By.ID, ID_LOGIN_CREDENTIALS, "visual_user"),

    # 🔐 Bloque de contraseñas
    (By.CLASS_NAME, CLASS_LOGIN_PASSWORD, "Password for all users:"),
    (By.CLASS_NAME, CLASS_LOGIN_PASSWORD, "secret_sauce"),

    # 🧭 Inputs y botones principales (valida solo existencia)
    (By.ID, "user-name", ""),
    (By.ID, "password", ""),
    (By.ID, "login-button", ""),

    # 🏷️ Logo o encabezado
    (By.CLASS_NAME, "login_logo", "Swag Labs"),
]

LOGIN_HEADER_ELEMENTS = [
    (By.CLASS_NAME, CLASS_LOGIN_LOGO, LANDING_MESSAGE),
    (By.CLASS_NAME, CLASS_STORE_TITLE, None),
]

# =====================================================
# 🧾 Textos esperados
# =====================================================
LANDING_MESSAGE = "Swag Labs"

TEXTS = {
    "login": {
        "error_generic": "Epic sadface: Username and password do not match any user in this service",
        "error_locked": "Epic sadface: Sorry, this user has been locked out.",
        "error_user_required": "Epic sadface: Username is required",
        "error_password_required": "Epic sadface: Password is required",
    },
    "inventory": {
        "title": "Products",
    },
}

# =====================================================
# 🔐 Datos de prueba
# =====================================================
VALID_USER = "standard_user"
VALID_PASS = "secret_sauce"
LOCKED_USER = "locked_out_user"
INVALID_USER = "fake_user"
INVALID_PASS = "wrong_pass"

LOGIN_TEST_SETS = {
    "invalid_inputs": [
        ("", "", CSS_ERROR_MESSAGE, TEXTS["login"]["error_user_required"]),
        (VALID_USER, "", CSS_ERROR_MESSAGE, TEXTS["login"]["error_password_required"]),
        (INVALID_USER, INVALID_PASS, CSS_ERROR_MESSAGE, TEXTS["login"]["error_generic"]),
    ],
    "valid_users": [
        (VALID_USER, VALID_PASS, True, "smoke"),
        (LOCKED_USER, VALID_PASS, False, "negative"),
        ("problem_user", VALID_PASS, True, "ui"),
        ("performance_glitch_user", VALID_PASS, True, "performance"),
        ("error_user", VALID_PASS, True, "regression"),
        ("visual_user", VALID_PASS, True, "ui"),
    ],
}

# =====================================================
# 🧩 Estructura de elementos de la pantalla de Login
# =====================================================
LOGIN_ELEMENTS = [
    # 🧠 Bloque de credenciales de usuario
    (By.ID, ID_LOGIN_CREDENTIALS, "Accepted usernames are:"),
    (By.ID, ID_LOGIN_CREDENTIALS, "standard_user"),
    (By.ID, ID_LOGIN_CREDENTIALS, "locked_out_user"),
    (By.ID, ID_LOGIN_CREDENTIALS, "problem_user"),
    (By.ID, ID_LOGIN_CREDENTIALS, "performance_glitch_user"),
    (By.ID, ID_LOGIN_CREDENTIALS, "error_user"),
    (By.ID, ID_LOGIN_CREDENTIALS, "visual_user"),

    # 🔐 Bloque de contraseñas
    (By.CLASS_NAME, CLASS_LOGIN_PASSWORD, "Password for all users:"),
    (By.CLASS_NAME, CLASS_LOGIN_PASSWORD, "secret_sauce"),

    # 🧭 Inputs y botón principal
    (By.ID, ID_USERNAME, ""),        # campo usuario
    (By.ID, ID_PASSWORD, ""),        # campo contraseña
    (By.ID, ID_LOGIN_BUTTON, ""),    # botón login

    # 🏷️ Encabezado visual
    (By.CLASS_NAME, CLASS_LOGIN_LOGO, LANDING_MESSAGE),
]

# ============================================================
# 👤 Credenciales
# ============================================================
VALID_PASS = "secret_sauce"
VALID_USER = "standard_user"
LOCKED_USER = "locked_out_user"
INVALID_USER = "fake_user"
INVALID_PASS = "wrong_pass"


# ============================================================
# 🧪 Datasets para pruebas parametrizadas
# ============================================================
LOGIN_TEST_DATA = [
    # username, password, should_succeed, selector, expected_message, mark_type
    ("", "", False, CSS_ERROR_MESSAGE, "Epic sadface: Username is required", "negative"),
    ("standard_user", "", False, CSS_ERROR_MESSAGE, "Epic sadface: Password is required", "negative"),
    ("invalid_user", "invalid_pass", False, CSS_ERROR_MESSAGE, "Epic sadface: Username and password do not match any user in this service", "negative"),
    ("locked_out_user", VALID_PASS, False, CSS_ERROR_MESSAGE, "Epic sadface: Sorry, this user has been locked out.", "negative"),
    ("standard_user", VALID_PASS, True, None, None, "smoke"),
    ("problem_user", VALID_PASS, True, None, None, "ui"),
    ("performance_glitch_user", VALID_PASS, True, None, None, "performance"),
    ("error_user", VALID_PASS, True, None, None, "regression"),
    ("visual_user", VALID_PASS, True, None, None, "ui"),
]

# ======================================================
# 🎯 PATRONES DE VALIDACIÓN (RegEx)
# ======================================================

VALIDATION_PATTERNS = {
    "letters": r'^[a-zA-Z]+$',
    "numbers": r'^\d+$',
    "alphanumeric": r'^[a-zA-Z0-9]+$',
    "email": r'^[\w\.-]+@[\w\.-]+\.\w+$',
    "no_spaces": r'^[^\s]+$'
}

# ============================================================
# 🛒 Elementos de productos
# ============================================================

#* Botones principales
BTN_ADD_TO_CART = "btn_inventory"
BTN_CART_LINK = "shopping_cart_link"

CATALOG_ELEMENTS = [
        (BY_CLASS, "inventory_item", None),
        (BY_CLASS, "inventory_item_name", None),
        (BY_CLASS, "inventory_item_price", None),
        (BY_CLASS, "btn_inventory", None),
    ]

CART_ELEMENTS = [
    (BY_CLASS, "cart_list", None),
    (BY_CLASS, "cart_quantity_label", "QTY"),
    (BY_CLASS, "cart_desc_label", "Description"),
    (BY_CLASS, "cart_item", None),
]

#* Catálogo
PRODUCT_URL = "inventory.html"
BTN_ADD_TO_CART = "btn_inventory"
BTN_CART_LINK = "shopping_cart_link"

#* Carrito
CART_URL = "cart.html"

TEXTS = {
    "inventory": {
        "title": "Products",
    },
    "cart": {
        "title": "Your Cart",
    },
}



# ============================================================
# 🕒 Timeout
# ============================================================
TIMEOUT = 5