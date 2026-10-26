from pymsgbox import confirm
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from conftest import open_pack, import_pack, announcement_buttons
import time
#NOTIFICATION: Так как некоторые действия по типу переключений карт происходят в доли секунды, тут расставлены тайм слипы для возможности увидеть все живому человеку

with webdriver.Chrome() as browser:
    browser.maximize_window()
    browser.implicitly_wait(2)
    browser.get('https://wikigacha.com')
    wait = WebDriverWait(browser, 15)

    # если есть что-то, что нужно конфермнуть
    announcement_buttons(browser)

    # клик по паку
    open_pack(browser, wait)

    #Переход на вкладку коллекции
    time.sleep(3)

    tab_collection_button = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//button[contains(., 'Collection')]")
    ))
    browser.execute_script("arguments[0].click();", tab_collection_button)
    print('Переход на вкладку произведен')


    #добавляем инфу о другой коллекции  (БУДЕТ ПЕРЕЗАГРУЗКА С ПЕРЕНОСОМ НА ПЕРВУЮ СТРАНИЦУ!
    # Обязательно нужно повторить предыдущие шаги!)
    import_pack(browser, wait)
    time.sleep(3)

    # если есть что-то, что нужно конфермнуть
    announcement_buttons(browser)

    # клик по паку
    open_pack(browser, wait)

    # Переход на вкладку коллекции
    time.sleep(3)

    tab_collection_button = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//button[contains(., 'Collection')]")
    ))
    browser.execute_script("arguments[0].click();", tab_collection_button)
    print('Переход на вкладку произведен')

    time.sleep(3)


    #Sort_by_category_button = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'CATEGORY')]"))).click()
   # print('Сортировка карт по категориям произведена')

    #time.sleep(2)

    #search_by_title_input = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search by title...']")))
    #search_by_title_input.send_keys("P")

    #time.sleep(2)

    #search_by_category_input = WebDriverWait(browser, 20).until(
        #EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search by category...']")))
    #search_by_category_input.send_keys("City")
    #time.sleep(2)

    #Нижнее переключение страниц коллекции

    #next_button = WebDriverWait(browser, 20).until(
    #    EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Next')]"))).click()
    #time.sleep(2)
    #prev_button = WebDriverWait(browser, 20).until(
    #    EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Prev')]"))).click()

    #time.sleep(2)
    #print('Переключение между страницами произошло успешно')

    #Быстрый переход на нужную страницу
    page_num_input = WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='number']"))
    )
    page_num_input.clear()
    page_num_input.send_keys("5")
    page_num_input.send_keys(Keys.ENTER)
    print('переход на страницу произведен')
    time.sleep(3)


    #Переключение языка
    #lang_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Work Language']")))
    #browser.execute_script("arguments[0].click();", lang_button)

    #time.sleep(2)

    #japanese_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@role='menuitemradio' and .//text()[contains(., 'Japanese')]]")))
    #browser.execute_script("arguments[0].click();", japanese_button)


