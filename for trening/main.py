from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://192.168.200.74:204/"
login_email = "test"
login_password = "Passw0rd"

try:
    browser = webdriver.Chrome("chromedriver\chromedriver.exe")  # подключаем webdriver.Chrome, указываем к нему путь.
    browser.get(link)  # Открываем инстанс
    '''time.sleep(5)  # устанавливаем задержку при открытии, чтобы успели загрузиться все элементы'''

    browser.implicitly_wait(30) # говорим WebDriver искать каждый элемент в течение 5 секунд
    elements = browser.find_elements(By.CSS_SELECTOR, '.row.no-gutters')
    if len(elements) == 6:
        print('Все элементы отображаются на странице авторизации. УСПЕШНАЯ ПРОВЕРКА')
    else:
        print('!!!!ПРОВЕРКА НЕ ПРОШЛА. НЕ ВСЕ ЭЛЕМЕНЫ ОТОБРАЖАЮТСЯ НА СТРАНИЦЕ АВТОРИЗАЦИИ!!!!')
    au_text = browser.find_element(By.CSS_SELECTOR, '.login-bg .row.no-gutters.align-items-center').text
    if au_text == "Вход в систему":
        print('На странице авторизации отображается корректный текст. УСПЕШНАЯ ПРОВЕРКА')
    else:
        print('!!!!ПРОВЕРКА НЕ ПРОШЛА. НЕ КОРРЕКТНЫЙ ТЕКСТ НА СТРАНИЦЕ АВТОРИЗАЦИИ!!!!')
    button = browser.find_element(By.CSS_SELECTOR, '.btn').text
    if button == "Войти":
        print('Текст кнопки входа отображается корректно. УСПЕШНАЯ ПРОВЕРКА')
    else:
        print('!!!!ПРОВЕРКА НЕ ПРОШЛА. НЕ КОРРЕКТНОЕ НАЗВАНИЕ КНОПКИ ВОЙТИ!!!!')
    input1 = browser.find_element(By.CSS_SELECTOR, 'input.form-control')  # ищем элемент для ввода логина
    input1.send_keys(login_email)  # вводим логин в поле
    time.sleep(1)  # устанавливаем задержку для визуальной проверки введнного текста, далее нужно убрать
    input2 = browser.find_element(By.CSS_SELECTOR, '[type = "password"]')  # ищем элемент для ввода пароля
    input2.send_keys(login_password) # вводим пароль в поле
    time.sleep(1)  # устанавливаем задержку для визуальной проверки введнного текста, далее нужно убрать
    button = browser.find_element(By.CSS_SELECTOR, '.btn')  # ищем кнопку для авторизации
    button.click()  # кликаем на кнопку авторизации
    if browser.find_element(By.CSS_SELECTOR, 'i.col-auto'):
        print("Авторизация удалась. УСПЕШНАЯ ПРОВЕРКА")  # выводим сообщение в консоль при успешной автоизации
    else:
        print("!!!!ПРОВЕРКА НЕ ПРОШЛА. АВТОРИЗАЦИЯ ПРОВАЛИЛАСЬ!!!!")  # выводим сообщение в консоль при успешной автоизации

    button_exit_1 = browser.find_element(By.CSS_SELECTOR, 'i.col-auto')
    button_exit_1.click()
    time.sleep(1) #устанавливаем задержку для визуальной проверки введнного текста, далее нужно убрать
    button_exit_2 = browser.find_element(By.CSS_SELECTOR, 'a.col.nav-link')
    button_exit_2.click()
    au_text = browser.find_element(By.CSS_SELECTOR, '.login-bg .row.no-gutters.align-items-center')
    '''time.sleep(1) #устанавливаем задержку чтобы браузер успел разлогиниться'''
    print("Разлогирование прошло успешно. УСПЕШНАЯ ПРОВЕРКА")

# негативные проверки авторизации
    browser.get(link)  # Открываем инстанс
    input1_1 = browser.find_element(By.CSS_SELECTOR, 'input.form-control')  # ищем элемент для ввода логина
    input1_1.send_keys(login_email)  # вводим логин в поле
    input2_1 = browser.find_element(By.CSS_SELECTOR, '[type = "password"]')  # ищем элемент для ввода пароля
    input2_1.send_keys(login_password, "1")  # вводим неправильный пароль в поле
    time.sleep(1)  #устанавливаем задержку для визуальной проверки введнного текста, далее нужно убрать
    button = browser.find_element(By.CSS_SELECTOR, '.btn')  # ищем кнопку для авторизации
    button.click()  # кликаем на кнопку авторизации
    '''time.sleep(2)  #устанавливаем задержку для визуальной проверки введнного текста, далее нужно убрать
    text_alarm = browser.find_element(By.CSS_SELECTOR, '[class = "row no-gutters align-items-center justify-content-center"]').text
    if text_alarm == "Неверный логин или пароль":
        print("С некорректным паролем авторизация не проходит. УСПЕШНАЯ ПРОВЕРКА")  # выводим сообщение в консоль
    else:
        print("!!!!ПРОВЕРКА С НЕКОРРЕКТНЫМ ПАРОЛЕМ НЕ ПРОШЛА!!!!")'''
    if WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '[class = "row no-gutters align-items-center justify-content-center"]'),'Неверный логин или пароль')):  # Ожидание проверки наличия данного текста в указанном элементе.
        print("С некорректным паролем авторизация не проходит. УСПЕШНАЯ ПРОВЕРКА")  # выводим сообщение в консоль
    else:
        print("!!!!ПРОВЕРКА С НЕКОРРЕКТНЫМ ПАРОЛЕМ НЕ ПРОШЛА!!!!")
    browser.get(link)  # Открываем инстанс
    input1_2 = browser.find_element(By.CSS_SELECTOR, 'input.form-control')  # ищем элемент для ввода логина
    input1_2.send_keys(login_email, "1")  # вводим неправильный логин в поле
    input2_2 = browser.find_element(By.CSS_SELECTOR, '[type = "password"]')  # ищем элемент для ввода пароля
    input2_2.send_keys(login_password)  # вводим пароль в поле
    time.sleep(1)  #устанавливаем задержку для визуальной проверки введнного текста, далее нужно убрать
    button = browser.find_element(By.CSS_SELECTOR, '.btn')  # ищем кнопку для авторизации
    button.click()  # кликаем на кнопку авторизации
    '''time.sleep(2)  # устанавливаем задержку
    text_alarm = browser.find_element(By.CSS_SELECTOR, '[class = "row no-gutters align-items-center justify-content-center"]').text
    if text_alarm == "Неверный логин или пароль":
        print("С некорректным логином авторизация не проходит. УСПЕШНАЯ ПРОВЕРКА")  # выводим сообщение в консоль
    else:
        print("!!!!ПРОВЕРКА С НЕКОРРЕКТНЫМ ЛОГИНОМ НЕ ПРОШЛА!!!!")'''
    if WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '[class = "row no-gutters align-items-center justify-content-center"]'),'Неверный логин или пароль')):  # Ожидание проверки наличия данного текста в указанном элементе.
        print("С некорректным логином авторизация не проходит. УСПЕШНАЯ ПРОВЕРКА")  # выводим сообщение в консоль
    else:
        print("!!!!ПРОВЕРКА С НЕКОРРЕКТНЫМ ЛОГИНОМ НЕ ПРОШЛА!!!!")



finally:
    # закрываем браузер после всех манипуляций
    browser.close()
    browser.quit()


