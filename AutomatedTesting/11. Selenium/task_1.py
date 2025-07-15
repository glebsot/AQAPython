# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_news_tensor(start_driver):
    saby_site = 'https://saby.ru/'
    start_driver.get(saby_site)
    assert start_driver.current_url == saby_site, 'Переход на saby.ru не осуществлен, либо неверный адрес сайта'
    contacts = WebDriverWait(start_driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.sbisru-Header-ContactsMenu'))
    )  # Проверяем что элемент видимый и кликабелен
    contacts.click()
    link_office = start_driver.find_element(By.CSS_SELECTOR, '[href = "/contacts"] span')
    link_office.click()
    contacts_url = 'https://saby.ru/contacts'
    assert start_driver.current_url == contacts_url, 'Переход на вкладку "контакты" не осуществлен, либо неверный ' \
                                                     'адрес '
    logo_tensor = WebDriverWait(start_driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.sbisru-Contacts__logo-tensor')))
    logo_tensor.click()
    start_driver.switch_to.window(start_driver.window_handles[1])
    tensor_url = 'https://tensor.ru/'
    assert start_driver.current_url == tensor_url, 'Не произведен переход на tensor.ru, либо неверный url'
    news_block4 = WebDriverWait(start_driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.tensor_ru-Index__block4-content'))
    )
    WebDriverWait(start_driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.tensor_ru-Index__block4-content'))
    )
    actions = ActionChains(start_driver)
    actions.move_to_element(news_block4).perform()  # Добавил скролл до элемента чтоб понятно было куда смотрим
    assert news_block4.is_displayed(), 'Отсутствует блок 4 с новостью "Сила в людях"'
    link_about = start_driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-bg [href="/about"]')
    link_about.click()
    saby_site_about = 'https://tensor.ru/about'
    assert start_driver.current_url == saby_site_about
    print('Автотест пройден')
    # sleep(3)
