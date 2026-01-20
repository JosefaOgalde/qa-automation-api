# QA Automation API (Pytest + Requests)

Proyecto sencillo para **QA Junior / Backend Junior**: pruebas automatizadas a una API pública usando `pytest` + `requests`, con configuración centralizada y reporte HTML.

## Qué vas a practicar
- Validaciones básicas de API: **status codes**, **JSON shape**, datos esperados
- Organización de un proyecto de automation (config, tests, reporting)
- Buenas prácticas mínimas para portfolio (README + bug report template)

## Estructura
- `src/config.py`: configuración (base URL, timeout, endpoints)
- `tests/test_posts_api.py`: tests del endpoint `/posts`
- `bug-reports/`: plantilla para reportar bugs
- `pytest.ini`: configuración de pytest
- `requirements.txt`: dependencias

## Requisitos
- Python 3.11+ recomendado

## Instalación (Windows PowerShell)
Desde la raíz del proyecto:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Ejecutar tests

```powershell
pytest
```

## Reporte HTML

```powershell
pytest --html=report.html --self-contained-html
```

Luego abre `report.html` con tu navegador.

## 🧪 Testing

Este proyecto incluye pruebas automatizadas de API utilizando `pytest`.

- Se validan códigos de estado (200, 201, 404).
- Se valida la estructura de las respuestas JSON.
- Se incluyen casos felices y casos de error.

### Observaciones QA
Se agregó un test que valida que el endpoint de posts retorne una lista no vacía.
Actualmente este test falla debido a que el entorno de pruebas no contiene datos iniciales,
lo cual se documenta como comportamiento esperado del entorno y no como un bug funcional.

Para evidenciar el trabajo realizado se generaron:
- Un primer reporte `report.html` con la ejecución base de los tests.
- Un segundo reporte (por ejemplo `report_v2.html`) para capturar la ejecución del nuevo escenario y comparar resultados.

## Configuración por variables de entorno
Podés cambiar el API base sin tocar código:

```powershell
$env:BASE_URL="https://jsonplaceholder.typicode.com"
$env:HTTP_TIMEOUT_SECONDS="10"
pytest
```

## Paso a paso (muy detallado) para recrearlo sola

### 1) Crear el proyecto y el entorno virtual
1. Crea una carpeta: `qa-automation-api`
2. Abre la carpeta en Cursor
3. Crea y activa el entorno virtual:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2) Crear `requirements.txt`
1. Crea un archivo `requirements.txt`
2. Agrega dependencias:
   - `pytest`: framework de test
   - `requests`: cliente HTTP
   - `pytest-html`: reporte en HTML
   - `ruff`: formateo/lint opcional
3. Instala:

```powershell
pip install -r requirements.txt
```

### 3) Crear configuración de pytest (`pytest.ini`)
1. Crea `pytest.ini`
2. Define:
   - `testpaths = tests` para que pytest busque tests ahí
   - `addopts = -q` para salida más corta

### 4) Crear `src/config.py`
1. Crea carpeta `src/` y archivo `config.py`
2. Define:
   - `BASE_URL` (por defecto: JSONPlaceholder)
   - `HTTP_TIMEOUT_SECONDS`
   - endpoints como `POSTS_ENDPOINT`
3. Importante: leer variables de entorno para que el código sea flexible.

### 5) Crear los tests en `tests/`
1. Crea carpeta `tests/` y archivo `test_posts_api.py`
2. Escribe tests simples y claros:
   - `GET /posts` devuelve 200 y lista
   - `GET /posts/1` devuelve 200 y tiene `id`, `userId`, `title`, `body`
   - `GET /posts/999999` devuelve 404
   - `POST /posts` devuelve 201 y “echo” del payload
3. Buenas prácticas:
   - Un test = una intención clara
   - Asserts cortos y con datos explícitos
   - Reusar `BASE_URL` y `timeout` desde `src/config.py`

### 6) Ejecutar
1. Corre:

```powershell
pytest
```

2. Si querés reporte:

```powershell
pytest --html=report.html --self-contained-html
```

### 7) Documentación (para portfolio)
1. Agrega `README.md` (qué hace, cómo correrlo)
2. Agrega `bug-reports/bug_report_template.md` para mostrar criterio QA

