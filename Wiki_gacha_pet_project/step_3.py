from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from conftest import open_pack, import_pack, announcement_buttons, table_chooser
import time
from selenium.webdriver.common.action_chains import ActionChains
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
        (By.XPATH, "//button[contains(., 'Battle')]")
    ))
    browser.execute_script("arguments[0].click();", tab_collection_button)
    print('Переход на вкладку произведен')

    time.sleep(3)

    browser.find_element(
        By.XPATH,
        "//button[.//p[contains(text(), 'Daily Raid Battle')]]"
    ).click()
    time.sleep(3)

    challenge_button = browser.find_element(
    By.XPATH,
    "//button[normalize-space()='Challenge Raid Boss']"
).click()
    time.sleep(3)

    #Party Selection
    Sorting = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(., 'ATK+DEF')]")
    )).click()
    time.sleep(3)

    table_chooser(browser)
    time.sleep(3)


    Select_top_ten_button = browser.find_element(
        By.XPATH,
        "//button[normalize-space()='Select Top 10']"
    ).click()
    time.sleep(3)

    raid_button = browser.find_element(By.XPATH, "//button[contains(., 'Start Raid')]").click()

    time.sleep(3)

    slider = browser.find_element(
        By.XPATH,
        "//input[@type='range']"
    )

    actions = ActionChains(browser)

    actions.click_and_hold(slider).perform()

    for _ in range(5):
        actions.move_by_offset(5, 0).perform()
        time.sleep(0.02)

    actions.release().perform()

    time.sleep(5)






