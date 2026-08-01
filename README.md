# Selenium Automation

## 프로젝트 소개

QA 업무에서 반복적으로 수행했던 API 관리 작업의 자동화 경험을 바탕으로
Python과 Selenium을 활용해 포트폴리오 용도로 재구성한 프로젝트입니다.
여러 프로젝트의 API 상태를 반복적으로 확인하고 관리해야 하는 작업이 있어 동일한 작업을 반복적으로 수행해야 했습니다.

이를 위해
프로젝트별 API 상태를 확인하고,
서비스 상태가 "완료"인 API를 자동으로 탐색하여 중지하도록 구현했습니다.
API가 존재하지 않는 프로젝트는 자동으로 건너뛰고 다음 프로젝트를 탐색하도록
예외 처리를 적용하여 반복 작업의 일관성과 효율성을 높였습니다.

> 본 프로젝트는 실제 QA 업무에서 수행했던 자동화 경험을 바탕으로
> 포트폴리오 용도로 재구성한 예제입니다.
> 회사의 내부 URL, 계정 정보 및 비공개 데이터는 포함하지 않습니다.

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

### 1. 저장소 Clone

```bash
git clone https://github.com/Uhm-Tree/selenium-automation.git
cd selenium-automation
```

### 2. 패키지 설치
```bash
pip install -r requirements.txt
```

### 3. 테스트 환경 설정

config.py의 URL을 테스트할 웹 환경에 맞게 설정합니다.
>공개 저장소에는 실제 업무 환경의 URL 및 인증 정보를 포함하지 않습니다.

### 4. 실행
```bash
python main.py
```


## 결과

- 반복적인 API 관리 작업을 Selenium 기반으로 자동화
- API가 존재하지 않는 프로젝트를 자동으로 건너뛰도록 예외 처리
- 특정 프로젝트에서 Timeout이 발생해도 다음 프로젝트 탐색을 계속하도록 개선


## 개선 내용

기존

- API가 존재하지 않는 프로젝트에서는 대상 요소를 찾지 못해
Timeout이 발생하면서 전체 자동화가 중단

개선 후

- TimeoutException을 처리하고 다음 프로젝트를 탐색하도록 로직을 개선

## 개선 이유

API가 존재하지 않는 프로젝트에서는 Timeout이 발생하여
자동화가 중단되는 문제가 있었습니다.

TimeoutException을 처리하고 드롭다운 메뉴를 다시 탐색하도록 개선하여
API가 없는 프로젝트도 자동으로 건너뛰고
모든 프로젝트를 연속적으로 처리할 수 있도록 개선했습니다.

## 배운 점

- Selenium을 활용한 반복 업무 자동화
- TimeoutException을 활용한 예외 상황 처리
- 기능별 Python 모듈화를 통한 코드 구조 개선
- 반복 작업 자동화 과정에서 예외 상황과 유지보수성을 고려하는 방법

