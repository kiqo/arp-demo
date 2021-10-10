from typing import Union
from pathlib import Path

from fastapi.testclient import TestClient
import pytest

from arpdemo.config import Settings
from arpdemo.main import app, get_settings


@pytest.fixture
def testdata():
    def _testdata(filepath: Union[str, Path]):
        return Path(__file__).parent / "tests" / "data" / filepath

    return _testdata


@pytest.fixture
def client(testdata):
    def _get_settings_override():
        return Settings(app_name="Test app name",
                        data_folder=testdata(""))
    client = TestClient(app)
    app.dependency_overrides[get_settings] = _get_settings_override
    return client


