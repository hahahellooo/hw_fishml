import numpy as np
from collections import Counter
from sklearn.neighbors import KNeighborsClassifier

# 사용자로부터 길이와 무게를 입력받는 함수
def input_data():
    length = float(input("길이를 입력하세요: "))
    weight = float(input("무게를 입력하세요: "))
    return [length, weight]

# 메인 함수
def main():
    training_data = []  # [(특징값, 라벨)]
    targets = []
    k = 5  # K값을 5로 설정
    while True:
        data = input_data()
        
        if training_data:
            # 예측
            prediction = predict(training_data, data)
            print(f"예측한 결과: {prediction}")
            
            # 예측 결과에 대한 사용자 피드백 받기
            feedback = input("예측한 결과가 맞나요?(Y/N): ")
            training_data.append(data)
            targets.append(feedback)
        else:
            # 훈련 데이터가 없을 때는 데이터 추가
            print("훈련 데이터가 없습니다. 데이터를 입력해주세요.")
            feedback = input("정답 (예: 도미/빙어): ")
            training_data.append(data)
            targets.append(feedback)

# 프로그램 실행
if __name__ == "__main__":
    main()

