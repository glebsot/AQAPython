from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains

sbis_site = 'https://fix.saby.ru/'
sbis_title = 'Saby — экосистема для управления бизнесом. СБИС теперь Саби'
driver = webdriver.Chrome()
try:
    driver.get(sbis_site)
    # driver.maximize_window()
    sleep(2)
    assert driver.current_url == sbis_site, 'Неверный URL'
    assert driver.title == sbis_title, 'Заголовок куку'
    tabs = driver.find_elements(By.CSS_SELECTOR, '.sbisru-Header__menu-item')
    assert len(tabs) == 5, 'Сколько надо'

    sleep(2)
    start_btn = driver.find_element(By.CSS_SELECTOR, '.sbisru-Header__request-button')
    start_btn_txt = 'Начать работу'
    assert start_btn.text == start_btn_txt, 'Неверный текст кнопки'
    assert start_btn.get_attribute('title') == start_btn_txt, 'Неверный текст по ховеру'
    assert start_btn.is_displayed(), 'Кнопки нет на экране'
    start_btn.click()

    driver.switch_to.window(driver.window_handles[1])
    sleep(2)
    login = driver.find_element(By.CSS_SELECTOR, '[data-qa="controls-Render__field"] input')
    login.send_keys('Сотникбезфич', Keys.ENTER)
    assert login.get_attribute('value') == 'Сотникбезфич', 'Логин не ввелся'
    password = driver.find_element(By.CSS_SELECTOR, '[type="password"]')
    password.send_keys('Пароль123', Keys.ENTER)
    sleep(4)
    presto = driver.find_element(By.CSS_SELECTOR, '[title="Автоматизации ресторанов, кафе, столовых и других форм общепита"]')
    presto.click()
    sleep(4)
    widget = driver.find_element(By.CSS_SELECTOR, '[title="Бонусы"]')
    action_chains = ActionChains(driver)
    sleep(2)
    action_chains.move_to_element(widget)
    action_chains.click(widget)
    action_chains.perform()
    print('Автотест пройден')
finally:
    driver.quit()