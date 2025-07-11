from datetime import datetime
import time
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
    start = time.time()
    yield
    finish = time.time()
    print(f'\nВремя выполнения метода: {finish-start}')
