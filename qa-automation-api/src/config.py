"""
Configuración central del proyecto.

Idea clave: los tests no deberían tener URLs "hardcodeadas" por todos lados.
Acá definimos:
- base URL del API bajo prueba
- timeouts
- endpoints

Para este proyecto usamos JSONPlaceholder (API pública) para practicar:
https://jsonplaceholder.typicode.com
"""

from __future__ import annotations

import os


def _env(name: str, default: str) -> str:
    value = os.getenv(name)
    return value if value not in (None, "") else default


# API pública para practicar (GET/POST/PUT/PATCH/DELETE "simulados")
BASE_URL: str = _env("BASE_URL", "https://jsonplaceholder.typicode.com")

# Timeout (segundos) para requests HTTP
HTTP_TIMEOUT_SECONDS: float = float(_env("HTTP_TIMEOUT_SECONDS", "10"))

# Endpoints (rutas relativas)
POSTS_ENDPOINT: str = "/posts"
COMMENTS_ENDPOINT: str = "/comments"

