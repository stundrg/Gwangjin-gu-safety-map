# gongmo

## 교통 관련 데이터 수집 후 최종 주제 선정

## 목적
- 교통사고 데이터를 분석해, 광진구에 특화된 정책을 제안하는 것이 목표입니다.
- 주제는 EDA를 통해 고령 보행자, 우회전 사고 등으로 좁혀갈 예정입니다.

## 📂 폴더 구조  

```plaintext
.
├── README.md               # 프로젝트 개요 (현재 파일)
├── pdm.lock                # PDM 환경 설정 파일
├── pyproject.toml          # 패키지 & Python 환경 설정
├── src/
│   ├── configs/            # 환경 설정 파일 (.env, config.json)
│   ├── data/               # 원본 데이터 및 가공 데이터 저장
│   ├── docs/               # 보고서, 논문, 발표자료
│   ├── gongmo/             # 공모전 관련 코드 (분석, 모델링)
│   │   ├── __init__.py
│   ├── logs/               # 로그 파일 저장
│   ├── notebooks/          # Jupyter Notebook (EDA, 분석)
│   ├── references/         # 참고 논문 및 자료
│   ├── results/            # 분석 결과 저장 (시각화, CSV 등)
│   ├── scripts/            # 데이터 처리 및 실행 코드
│   ├── tests/              # 테스트 코드
│   │   ├── __init__.py
└── tests/                  # 테스트 코드 (별도 테스트용)
    ├── __init__.py
