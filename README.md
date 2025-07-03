# EM Algorithm for Coin Parameter Estimation

EM 알고리즘을 사용하여 동전의 앞면 확률을 추정하는 프로그램입니다.

## 파일 구조

- `EM_coin_data.py` - 동전 데이터 생성기
- `EM_coin_Infer.py` - EM 알고리즘을 통한 확률 추정
- `coin_data.txt` - 생성된 동전 데이터
- `data_result.txt` - 추정 결과

## 사용법

### 1. 데이터 생성
```bash
python EM_coin_data.py
```

실행 시 입력 요구사항:
- 동전의 개수 (k)
- 각 동전의 앞면 확률 (공백으로 구분)
- 데이터 개수 (N)
- 각 데이터의 길이 (M)

### 2. 확률 추정
```bash
python EM_coin_Infer.py
```

`coin_data.txt` 파일을 읽어 EM 알고리즘으로 동전의 앞면 확률을 추정합니다.

## 출력 결과

- 추정된 동전별 확률
- 동전 분류 정확도
- `data_result.txt`에 상세 결과 저장

## 알고리즘 개요

1. **E-Step**: 각 데이터가 특정 동전에서 나왔을 확률(responsibility) 계산
2. **M-Step**: 계산된 확률을 바탕으로 동전의 앞면 확률 업데이트
3. 수렴할 때까지 반복

## 요구사항

- Python 3.x
- numpy
- pandas