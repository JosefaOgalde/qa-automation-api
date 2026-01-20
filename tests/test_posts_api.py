import requests

from src.config import BASE_URL, HTTP_TIMEOUT_SECONDS, POSTS_ENDPOINT


def _url(path: str) -> str:
    return f"{BASE_URL}{path}"


def test_get_posts_returns_200_and_list():
    """
    Objetivo: validar que /posts responde 200 y devuelve una lista JSON.
    """
    r = requests.get(_url(POSTS_ENDPOINT), timeout=HTTP_TIMEOUT_SECONDS)
    assert r.status_code == 200

    data = r.json()
    assert isinstance(data, list)
    assert len(data) > 0


def test_get_single_post_by_id_returns_expected_shape():
    """
    Objetivo: validar el contrato mínimo de un post.
    """
    r = requests.get(_url(f"{POSTS_ENDPOINT}/1"), timeout=HTTP_TIMEOUT_SECONDS)
    assert r.status_code == 200

    post = r.json()
    assert isinstance(post, dict)
    assert post["id"] == 1
    assert "userId" in post
    assert "title" in post
    assert "body" in post


def test_get_nonexistent_post_returns_404():
    """
    Objetivo: validar manejo de recurso inexistente.
    JSONPlaceholder devuelve 404 y body vacío para un id muy alto.
    """
    r = requests.get(_url(f"{POSTS_ENDPOINT}/999999"), timeout=HTTP_TIMEOUT_SECONDS)
    assert r.status_code == 404


def test_create_post_returns_201_and_echoes_payload():
    """
    Objetivo: validar creación (POST).
    Nota: JSONPlaceholder NO crea realmente, pero responde 201 con un id simulado.
    """
    payload = {"title": "qa-automation-api", "body": "hello", "userId": 1}
    r = requests.post(_url(POSTS_ENDPOINT), json=payload, timeout=HTTP_TIMEOUT_SECONDS)
    assert r.status_code == 201

    created = r.json()
    assert created["title"] == payload["title"]
    assert created["body"] == payload["body"]
    assert created["userId"] == payload["userId"]
    assert "id" in created

