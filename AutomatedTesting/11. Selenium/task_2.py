# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from time import sleep
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--disable-notifications")  # Отключаем нотификации

sbis_site = 'https://fix-online.sbis.ru/'
driver = webdriver.Chrome()
try:
    driver.get(sbis_site)
    driver.maximize_window()
    sleep(2)
    login = driver.find_element(By.CSS_SELECTOR, '[data-qa="controls-Render__field"] input')
    login.send_keys('Сотникбезфич', Keys.ENTER)
    sleep(2)
    password = driver.find_element(By.CSS_SELECTOR, '[type="password"]')
    password.send_keys('Пароль123', Keys.ENTER)
    sleep(5)
    contacts = driver.find_element(By.CSS_SELECTOR, '[href="/page/dialogs"]')
    actions = ActionChains(driver)
    actions.double_click(contacts).perform()
    sleep(4)
    message_button = driver.find_element(By.CSS_SELECTOR, '[data-qa="sabyPage-addButton"]')
    message_button.click()
    sleep(3)
    search_string = driver.find_element(By.CSS_SELECTOR, '[class="controls-StackTemplate-content"] input')
    # search_string.click()
    search_string.send_keys('Понимаев Андрей Константинович')
    sleep(3)
    recipient = driver.find_element(By.CSS_SELECTOR, '[title="Понимаев Андрей Константинович"]')
    recipient.click()
    sleep(3)
    input_field_message = driver.find_element(By.CSS_SELECTOR, '[data-qa="textEditor_base_editor"]')
    input_field_message.send_keys('Привет, друг!')
    sleep(2)
    button_msg = driver.find_element(By.CSS_SELECTOR, '[data-qa="msg-send-editor__send-button"]')
    button_msg.click()
    sleep(3)
    message_sender = driver.find_element(By.CSS_SELECTOR, '[data-qa="msg-dialogs-item__addressee"][title="Понимаев Андрей Константинович"]')
    assert message_sender.is_displayed()
    actions.context_click(message_sender).perform()
    sleep(3)
    delete_button = driver.find_elements(By.CSS_SELECTOR, '[title="Перенести в удаленные"] [class="ws-ellipsis '
                                                          'controls-Menu__content-wrapper_width"]')
    delete_button[0].click()
    sleep(3)
    empty_registry = driver.find_elements(By.CSS_SELECTOR, '[data-qa="hint-EmptyView__title"]')
    assert empty_registry, 'Сообщение не удалено'
    print('Автотест пройден')
finally:
    driver.quit()
