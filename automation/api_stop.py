# 메인 로직

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from utils.modal import click_confirm
from utils.dropdown import scroll_dropdown

from config import WAIT_TIME, SHORT_WAIT_TIME


def stop_all_api(driver):

    wait = WebDriverWait(driver, WAIT_TIME)
    short_wait = WebDriverWait(driver, SHORT_WAIT_TIME)

    index = 1

    while True:
        driver.execute_script("window.scrollTo(0, 0);")

        dropdown_btn = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//button[contains(@class,"selection-button")]')
            )
        )
        driver.execute_script("arguments[0].click();", dropdown_btn)

        menus = driver.find_elements(
            By.XPATH, '//li[contains(@class,"dropdown-item")]'
        )

        if index > len(menus):
            print("✅ 모든 프로젝트 API 중지 완료")
            break

        menu = menus[index - 1]
        menu_text = menu.text.strip()
        driver.execute_script("arguments[0].click();", menu)

        print(f"\n▶ 처리 중: {menu_text}")

               # API 정보가 없으면 2초간 대기한 후 다음 프로젝트로 넘어감    
        try:
                    short_wait.until(
                        EC.presence_of_element_located(
                            (By.XPATH, '//div[contains(@class,"tbody")]//tr')
                        )
                    )
        except TimeoutException:
                    print("⚠ API 정보 없음 → 다음 프로젝트로 이동")
        
                    # 다음 드롭다운 준비
                    driver.execute_script("arguments[0].click();", dropdown_btn)
                    scroll_dropdown(driver)
                    index += 1
                    continue
        
                # 완료 상태 전부 중지
        while True:
                    radios = driver.find_elements(
                        By.XPATH,
                        '//tr[td[contains(normalize-space(.),"완료")]]//input[@type="radio"]'
                    )
        
                    if not radios:
                        print("✅ API 정보가 없습니다.")
                        break
        
                    driver.execute_script("arguments[0].click();", radios[0])
        
                    driver.execute_script(
                        "arguments[0].click();",
                        wait.until(
                            EC.presence_of_element_located(
                                (By.XPATH, '//button[contains(text(),"서비스 중지")]')
                            )
                        )
                    )
        
                    click_confirm(driver)
                    click_confirm(driver)
        
                    # 🔴 중지 후 테이블 재로딩 대기
                    wait.until(
                        EC.presence_of_element_located(
                            (By.XPATH, '//div[contains(@class,"tbody")]//tr')
                        )
                    )
        
                    print("🛑 API 1개 중지 완료")
        
                # 다음 드롭 다운 준비
        driver.execute_script("arguments[0].click();", dropdown_btn)
        scroll_dropdown(driver)
        
        index += 1

        