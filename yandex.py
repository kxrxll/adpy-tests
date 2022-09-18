import requests


class Ya_disk:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def upload(self, path, url):
        headers = self.get_headers()
        params = {
            "path": path,
            "url": url
        }
        response = requests.post("https://cloud-api.yandex.net/v1/disk/resources/upload", params=params, headers=headers)
        response.raise_for_status()

    def check_connection(self):
        headers = self.get_headers()
        response = requests.get("https://cloud-api.yandex.net/v1/disk/", headers=headers)
        response.raise_for_status()
        return response.status_code
