import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException


def open_pack(browser, wait):
    try:
        browser.find_element(By.CSS_SELECTOR, "img[alt='Wiki Pack']").click()
        print('Клик по паку выполнен')

        wait.until(EC.presence_of_element_located(
            (By.XPATH, "//div[contains(@style, 'z-index: 120')]")
        ))
        time.sleep(2)
        print('карты отображены')

    except Exception as e:
        print(f'Ошибка при открытии пака: {e}')

def import_pack(browser, wait):
    try:
        time.sleep(2)
        import_collection_btn = browser.find_element(By.XPATH, "//button[contains(., 'Import')]").click()
        time.sleep(4)
        file_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
        file_input.send_keys(r"C:\Users\Rina\Desktop\Deepseak\wikigacha_backup_en_20261026_142611.wgbak")

        confirm_upload = browser.switch_to.alert
        confirm_upload.send_keys('Test12345678!')
        confirm_upload.accept()
        time.sleep(2)
        second_confirm = browser.switch_to.alert
        second_confirm.accept()

        print('коллекция загружена')
    except Exception as e:
        print(f'Ошибка при загрузке данных: {e}')


# если есть что-то, что нужно конфермнуть
def announcement_buttons(browser):
    dialogs = [
        (By.XPATH, "//button[.//p[text()='Соглашаюсь']]"),
        (By.XPATH, "//button[@aria-label='OK']"),
        (By.XPATH, "//button[normalize-space(translate(., 'GOTIT', 'gotit')) = 'got it']"),
        (By.XPATH, "//button[text()='OK']")
    ]

    max_attempts = 4  # Максимум попыток, чтобы избежать бесконечного цикла
    for attempt in range(max_attempts):
        closed = False
        for by, selector in dialogs:
            try:
                button = WebDriverWait(browser, 3).until(
                    EC.element_to_be_clickable((by, selector))
                )
                button.click()
                print(f"Клик по диалогу: {selector}")
                closed = True
                time.sleep(2)  # Небольшая пауза после клика
                break  # После клика начинаем проверку сначала (чтобы дать время следующему диалогу)
            except TimeoutException:
                continue
        if not closed:
            # Ни одного диалога не найдено – выходим
            break
    print("Все диалоги закрыты")


def table_chooser(browser):
    try:
        row = browser.find_element(
            By.XPATH,
            "//tbody/tr[.//button[text()='+'][not(@disabled)]]"
        )

        plus_btn = row.find_element(
            By.XPATH,
            ".//button[text()='+']"
        )

        plus_btn.click()

        minus_btn = row.find_element(
            By.XPATH,
            ".//button[text()='-']"
        )

        minus_btn.click()

        print('Добавление по одному проверено')

    except Exception as e:
        print(f'Ошибка: {e}')