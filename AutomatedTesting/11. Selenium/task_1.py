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
from time import sleep

saby_site = 'https://saby.ru/'
driver = webdriver.Chrome()
try:
    driver.get(saby_site)
    driver.maximize_window()
    sleep(3)
    contacts = driver.find_element(By.CSS_SELECTOR, '.sbisru-Header-ContactsMenu')
    contacts.click()
    sleep(2)
    link_office = driver.find_element(By.CSS_SELECTOR, '[href = "/contacts"] span')
    link_office.click()
    sleep(3)
    logo_tensor = driver.find_element(By.CSS_SELECTOR, '.sbisru-Contacts__logo-tensor')
    logo_tensor.click()
    sleep(5)
    driver.switch_to.window(driver.window_handles[1])
    news_block4 = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content')

    actions = ActionChains(driver)
    actions.move_to_element(news_block4).perform()  # Добавил скролл до элемента чтоб понятно было куда смотрим
    sleep(3)

    assert news_block4.is_displayed(), 'Отсутствует блок 4 с новостью "Сила в людях"'
    link_about = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-bg [href="/about"]')
    link_about.click()
    sleep(3)
    saby_site_about = 'https://tensor.ru/about'
    assert driver.current_url == saby_site_about
    print('Автотест пройден')
    sleep(3)
finally:
    driver.quit()
