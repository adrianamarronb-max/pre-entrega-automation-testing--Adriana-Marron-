# 🧪 Proyecto de Automatización con Selenium + Pytest

## 📋 Descripción general

Este proyecto forma parte de la **preentrega del curso de QA Automation con Selenium + Pytest**.  
Su objetivo es demostrar el dominio de buenas prácticas de automatización, estructuración modular del framework y generación de reportes.

La suite cubre flujos principales de la aplicación **SauceDemo**, incluyendo:
- Acceso y visualización de la página de login.
- Validación de credenciales (tests positivos y negativos).
- Acceso al catálogo de productos.
- Flujo de carrito de compras.
- Validaciones visuales, de texto y navegación.


---

## 🧱 Estructura del proyecto

```
preentrega/
├── tests/                    # Carpeta principal de tests
│   ├── test_login/           # Casos de prueba relacionados al login
│   ├── test_inventory/       # Casos de prueba del catálogo y carrito
│   └── __init__.py
│
├── utils/                    # Reutilizables (acciones, asserts, locators, etc.)
│   ├── assertions/           # Validaciones específicas (elementos, inputs, navegación)
│   ├── actions.py            # Funciones que ejecutan interacciones
│   ├── constants.py          # Constantes globales y datasets parametrizados
│   ├── locators.py           # Selectores centralizados
│   └── visuals.py
│
├── reports/                  # Reportes HTML generados automáticamente
├── conftest.py               # Configuración y hooks de Pytest
├── requirements.txt          # Dependencias del proyecto
├── pytest.ini                # Configuración de Pytest (marcas, paths, etc.)
├── run_tests.bat             # Script de ejecución automatizada (Windows)
├── run_tests.sh              # Script de ejecución automatizada (Linux/Mac)
└── README.md                 # Este archivo
```

---

## ⚙️ Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/manuelmarchena/pre-entrega-automation-testing-manuel-marchena.git
   cd preentrega-automation
   ```

2. Crear entorno virtual (opcional pero recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate    # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Ejecución de las pruebas

### ▶️ Ejecución completa
```bash
pytest -v -s --html=reports/report.html --self-contained-html
```

### 🔥 Ejecución por tipo de test

- **Smoke tests:**
  ```bash
  pytest -m smoke -v -s --html=reports/smoke_report.html --self-contained-html
  ```

- **Regression tests:**
  ```bash
  pytest -m regression -v -s --html=reports/regression_report.html --self-contained-html
  ```

- **Negative tests:**
  ```bash
  pytest -m negative -v -s --html=reports/negative_report.html --self-contained-html
  ```

---

## 🧰 Ejecución rápida con scripts

### 🪟 En Windows:
Ejecutar el archivo:
```bash
run_tests.bat
```

### 🐧 En Linux / macOS:
Dar permisos y ejecutar:
```bash
chmod +x run_tests.sh
./run_tests.sh
```

Ambos scripts generarán automáticamente reportes en la carpeta `/reports`.

> 💡 **Opcional**: Si prefieres no incluir los scripts en tu clonación, puedes descargarlos desde el repositorio auxiliar:
> - [Descargar run_tests.bat](https://github.com/manuelmarchena/test-auto-scripts)
> - [Descargar run_tests.sh](https://github.com/manuelmarchena/test-auto-scripts)

---

## ✅ Cobertura de pruebas

| Módulo | Tipo de prueba | Descripción | Resultado esperado |
|--------|----------------|--------------|--------------------|
| Login | Negativo | Validación de errores por usuario/contraseña vacíos o incorrectos | Mensajes de error visibles |
| Login | Positivo | Acceso correcto con usuarios válidos | Redirección a `/inventory.html` |
| Catálogo | Smoke | Validación de listado de productos y textos | Título “Products” visible |
| Carrito | Regression | Flujo de agregar productos y validar el total | Carrito actualizado correctamente |

---

## 🧾 Requisitos de la preentrega

✔️ Estructura modular con `actions`, `assertions`, `constants` y `tests`.  
✔️ Cobertura mínima de flujos principales de login, catálogo y carrito.  
✔️ Uso de `pytest` y `pytest-html` para reportes.  
✔️ Uso de `pytest.mark` para categorizar pruebas (smoke, regression, negative).  
✔️ Archivo `requirements.txt` con dependencias.  
✔️ Reporte HTML exportable.  
✔️ README documentado con instrucciones y scripts de ejecución.

---

## 👨‍💻 Autor

**Manuel Marchena**  
QA Analyst & Automation Engineer  
📧 [Contacto profesional](mailto:manuelmarche34@gmail.com)
