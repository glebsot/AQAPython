# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_message_to_yourself(start_driver):
    sbis_site = 'https://fix-online.sbis.ru/'
    start_driver.get(sbis_site)
    login = WebDriverWait(start_driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-qa="auth-AdaptiveLoginForm__login"] input')))
    assert login.is_displayed(), 'Поле логин не отображается'
    login = WebDriverWait(start_driver, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-qa="auth-AdaptiveLoginForm__login"] input')))
    login.send_keys('Логин', Keys.ENTER)
    password = WebDriverWait(start_driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '[type="password"]')))
    assert password.is_displayed(), 'Поле пароль не отображается'
    password = WebDriverWait(start_driver, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[type="password"]')))
    password.send_keys('Пароль', Keys.ENTER)
    page_loaded = WebDriverWait(start_driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-qa="NavigationPanels-Accordion__title"]')))
    assert page_loaded.is_displayed(), 'Страница не загружена'
    # assert start_driver.current_url == sbis_site, f'Переход на {sbis_site} не осуществлён'
    # ready_state = start_driver.execute_script("return document.readyState")
    # assert ready_state == 'complete', 'Страница не загружена'
    auth_cookie = start_driver.get_cookie("machine_name")
    assert auth_cookie is not None, "Сессионная cookie не найдена"
    actions = ActionChains(start_driver)
    WebDriverWait(start_driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-qa="Контакты"]')))
    contacts = WebDriverWait(start_driver, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-qa="Контакты"]')))
    actions.double_click(contacts).perform()
    contacts_url = 'https://fix-online.sbis.ru/page/dialogs'
    assert start_driver.current_url == contacts_url, "Не осуществлён переход в раздел 'Контакты'"
    message_button = WebDriverWait(start_driver, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-qa="sabyPage-addButton"]')))
    message_button.click()
    WebDriverWait(start_driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '[class="controls-StackTemplate-content"] input')))
    search_string = WebDriverWait(start_driver, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="controls-StackTemplate-content"] input')))
    search_string.send_keys('Понимаев Андрей Константинович')
    WebDriverWait(start_driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '[templatename="Addressee/popup:Stack"] [data-qa="item"]')))
    recipient = WebDriverWait(start_driver, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[templatename="Addressee/popup:Stack"] [data-qa="item"]')))
    recipient.click()
    WebDriverWait(start_driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-qa="textEditor_base_editor"]')))
    input_field_message = WebDriverWait(start_driver, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-qa="textEditor_base_editor"]')))
    input_field_message.send_keys('Привет, друг!')
    WebDriverWait(start_driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-qa="msg-send-editor__send-button"]')))
    button_msg = WebDriverWait(start_driver, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-qa="msg-send-editor__send-button"]')))
    button_msg.click()
    message_sender = WebDriverWait(start_driver, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-qa="msg-dialogs-item__addressee"][title="Понимаев Андрей '
                                                     'Константинович"]')))
    assert message_sender.is_displayed(), 'Сообщение не пришло'
    actions.context_click(message_sender).perform()
    delete_button = start_driver.find_elements(By.CSS_SELECTOR, '[title="Перенести в удаленные"] [class="ws-ellipsis '
                                                          'controls-Menu__content-wrapper_width"]')
    delete_button[0].click()
    empty_registry = start_driver.find_elements(By.CSS_SELECTOR, '[data-qa="hint-EmptyView__title"]')
    assert empty_registry, 'Сообщение не удалено'
    print('Автотест пройден')
