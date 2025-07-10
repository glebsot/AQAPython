from datetime import datetime

import pytest


@pytest.fixture(scope='class', autouse=True)
def start_stop_time_class():
    start = datetime.now().time()
    print(f'\nВремя начала выполнения класса: {start}')
    yield
    stop = datetime.now().time()
    print(f'\nВремя окончания выполнения класса: {stop}')


@pytest.fixture()
def start_stop_time_method():
    start = datetime.now().time()
    print(f'\nВремя начала выполнения метода: {start}')
    yield
    finish = datetime.now().time()
    print(f'\nВремя окончания выполнения метода: {finish}')
