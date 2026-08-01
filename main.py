## Ncloud beta-console VOT 에서 배포된 API 자동 중지 Selenium Automation
# 실행 파일

from selenium import webdriver
from config import URL
from automation.api_stop import stop_all_api


def main():

    # WebDriver 생성 (필수) 웹페이지를 자동화하기 위해 필요
    driver = webdriver.Chrome()

    # 사이트 접속
    driver.get(URL)


    print("브라우저 열림 - 로그인 대기 중")
    input("로그인 완료 후 Enter 키를 누르세요")


    try:

        stop_all_api(driver)

    # 예외 발생하면 동작 멈춤
    # 예외 발생 처리를 하는 이유는 런타임 오류 발생 시 프로그램이 강제 종료되는 것을 막고, 안정적으로 실행 흐름을 유지하며 적절한 오류 메시지를 제공하기 위해 필수임
    except Exception as e:
        print("\n❌ 예외 발생!")
        print(e)

        # 🔴 여기서 멈춰서 화면 유지
        input("\n에러 발생. 브라우저를 확인한 후 Enter를 누르세요")

    finally:
        driver.quit()    


if __name__ == "__main__":
    main()