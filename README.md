# Selenium Automation

## 프로젝트 소개

NAVER LABS QA 업무 중 반복적으로 수행하던
API 중지 작업을 Selenium으로 자동화한 프로젝트입니다.
배포된 API는 중지 후 삭제해야만
서버 리소스를 회수할 수 있어
동일한 작업을 반복적으로 수행해야 했습니다.

프로젝트별 API 상태를 조회하고,
서비스 상태가 "완료"인 API를 자동으로 중지하며,
API가 존재하지 않는 프로젝트는 자동으로 건너뛰도록 구현하여
반복 작업 시간을 줄이고 작업의 일관성과 효율을 높였습니다.

## 주요 기능

- 프로젝트 목록 자동 탐색
- 프로젝트별 API 조회
- 완료 상태 API 자동 탐색
- 서비스 중지 자동 수행
- API 미존재 프로젝트 자동 건너뛰기
- Confirmation Modal 자동 처리
- 예외 상황(Timeout) 처리

## 기술 스택

- Python
- Selenium
- Chrome WebDriver
- Git

## 프로젝트 구조

```text
selenium-automation
│
├── automation
│   └── api_stop.py
│
├── utils
│   ├── dropdown.py
│   └── modal.py
│
├── config.py
├── main.py
└── requirements.txt
```

## 실행 방법

```bash
pip install -r requirements.txt
python main.py
```

## 결과

- 반복적인 API 관리 작업 자동화
- API가 없는 프로젝트에서도 자동화 중단 없이 수행
- 예외 상황에서도 중단되지 않는 자동화 구현


## 개선 내용

기존

- API가 없는 프로젝트에서 Timeout 발생
- 자동화 중단

개선 후

- TimeoutException 처리
- API가 없는 프로젝트 자동 건너뛰기
- 자동화 연속 수행 가능

## 개선 이유

API가 존재하지 않는 프로젝트에서는 Timeout이 발생하여
자동화가 중단되는 문제가 있었습니다.

TimeoutException을 처리하고 드롭다운 메뉴를 다시 탐색하도록 개선하여
API가 없는 프로젝트도 자동으로 건너뛰고
모든 프로젝트를 연속적으로 처리할 수 있도록 개선했습니다.

## 배운 점

- Selenium을 활용한 반복 업무 자동화
- TimeoutException 기반 예외 처리
- Python 모듈화 및 프로젝트 구조 개선
- 유지보수를 고려한 코드 리팩토링
- 실제 QA 업무를 자동화하며 유지보수성과 생산성을 고려하는 개발 방식을 경험