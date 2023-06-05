import asyncio

import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from starlette.status import HTTP_404_NOT_FOUND, HTTP_422_UNPROCESSABLE_ENTITY
from unittest.mock import patch


@pytest.fixture(scope="session")
def event_loop():
    return asyncio.get_event_loop()


@pytest.fixture
async def app() -> FastAPI:
    from power_api.main import app, startup
    await startup()
    return app


@pytest.fixture
async def client(app: FastAPI) -> AsyncClient:
    async with AsyncClient(
        app=app,
        base_url="http://testserver",
        headers={"Content-Type": "/api/openapi"}
    ) as client:
        yield client


async def test_routes_exist(app: FastAPI, client: AsyncClient) -> None:
    with patch('power_api.drivers.power_drivers.PowerOutput.switch_off') as mock_my_function:
        res = await client.post(app.url_path_for("switch_chanel_off"), json={"chanel_number": 1})
        assert res.status_code != HTTP_404_NOT_FOUND
        assert res.status_code != HTTP_422_UNPROCESSABLE_ENTITY
        mock_my_function.assert_called()

