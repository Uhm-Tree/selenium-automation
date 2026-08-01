# 드롭다운 처리

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import WAIT_TIME


def scroll_dropdown(driver):
    wait = WebDriverWait(driver, WAIT_TIME)

    scroll_box = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, '//div[contains(@class,"scroll-box")]')
        )
    )

    driver.execute_script(
        "arguments[0].scrollTop = arguments[0].scrollHeight",
        scroll_box
    )