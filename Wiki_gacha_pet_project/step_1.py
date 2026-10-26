from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import pyperclip
from conftest import open_pack, announcement_buttons
import time
#NOTIFICATION: Так как некоторые действия по типу переключений карт происходят в доли секунды, тут расставлены тайм слипы для возможности увидеть все живому человеку

with webdriver.Chrome() as browser:
    browser.maximize_window()
    browser.implicitly_wait(2)
    browser.get('https://wikigacha.com')
    wait = WebDriverWait(browser, 15)

    time.sleep(10)


    #если есть что-то, что нужно конфермнуть
    announcement_buttons(browser)

    time.sleep(5)

    #клик по паку
    open_pack(browser, wait)

    #Смотрим выпавшие карты

    #right_shuffle = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Next card']"))).click()
    #time.sleep(3)
    #left_shuffle = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Previous card']"))).click()

    #time.sleep(3)
    #print('карты можно просмотреть')

    #Open_card_wiki_page = browser.find_element(By.XPATH, "(//div[contains(@class,'group')])[1]").click()
    #print('Страница открыта')
    #time.sleep(3)

    #copy_result = browser.find_element(By.XPATH, "//button[contains(., 'Copy Result')]").click()
    #time.sleep(3)
    #alert = browser.switch_to.alert.accept()

    #Печатаем инфу со скопированных карт

    #clipboard_text = pyperclip.paste()
    #print(f"Содержимое буфера обмена: {clipboard_text}")

    #sound_off = browser.find_element(By.XPATH,"//button[contains(@aria-label, 'Flip sound')]").click()
    #print('Звук выключен')
    #time.sleep(3)

    #view_mode_wide = browser.find_element(By.CSS_SELECTOR, "button[aria-label='View Mode: Stack']").click()
    #time.sleep(3)
    #view_mode_small = browser.find_element(By.CSS_SELECTOR, "button[aria-label='View Mode: Grid']").click()
   # print('Отображение меняется')

    #time.sleep(3)

    #шаффл через маленькие кнопки

    #small_back_shuffle = browser.find_element(By.XPATH,"//button[normalize-space() = '<' and not(@aria-label)]").click()
    #time.sleep(3)
    #small_forward_shuffle = browser.find_element(By.XPATH,"//button[normalize-space() = '>' and not(@aria-label)]").click()

    #print('Альтернативный шаффл работает')

    #Проверка достижений
    Trophy = browser.find_element(By.CSS_SELECTOR, "button[aria-label='Trophies']").click()
    time.sleep(2)

    scroll_container = browser.find_element(By.XPATH,"//div[contains(@class,'overflow-y-auto')]")
    browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight",scroll_container)
    print('прокрутка завершена')

    close_button_trophies = browser.find_element(By.XPATH,"//button[.//text()='✕']").click()
    time.sleep(2)

    info_button = browser.find_element(By.CSS_SELECTOR, "button[aria-label='Game Info']").click()
    time.sleep(2)

    info_scroll_container = browser.find_element(By.CSS_SELECTOR,"div.overflow-y-auto")
    browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight",info_scroll_container)

    print("прокрутка до низа завершена")

    close_button = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='✕']"))).click()

    time.sleep(2)













