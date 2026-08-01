# 모달 처리

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import WAIT_TIME


def click_confirm(driver):
    wait = WebDriverWait(driver, WAIT_TIME)

    modal = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, '//div[contains(@class, "modal")]')
        )
    )

    btn = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, '(//button[normalize-space(text())="확인"])[last()]')
        )
    )

    driver.execute_script("arguments[0].click();", btn)

    # 모달이 완전히 닫힐 때까지 대기
    wait.until(EC.staleness_of(modal))