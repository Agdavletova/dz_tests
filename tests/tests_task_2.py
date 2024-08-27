import requests
import pytest


class TestApiYandex():
    def setup_method(self):
        self.path = "https://cloud-api.yandex.net/v1/disk/resources?"
        self.headers = {
            "Authorization": "OAuth "
        }

    @pytest.mark.parametrize(
        "param, value, status",
        (
            ['path' , "New folder", 201],
            ["pa", "New", 401],
            ["path", 'New folder', 405]
        )
    )
    def test_create_folder(self, param, value, status):
        params = {param: value}
        response = requests.put(self.path, headers=self.headers, params=params)
        assert response.status_code == status
