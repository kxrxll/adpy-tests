import pytest
from yandex import Ya_disk
import configparser


def test_connection():
    config = configparser.ConfigParser()
    config.read('../settings.ini')
    yandex = Ya_disk(config["YaDisk"]["token"])
    assert yandex.check_connection() == 200
