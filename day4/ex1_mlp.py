import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.datasets import mnist

# 데이터 로드 및 전처리
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# 데이터를 0~1 범위로 정규화
x_train = x_train / 255.0
x_test = x_test / 255.0

# One-hot encoding for labels
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# MLP 모델 구축
model = Sequential([
    Flatten(input_shape=(28, 28)),  # 이미지를 1차원 배열로 변환
    Dense(128, activation='relu'),  # 첫 번째 Dense 레이어
    Dense(64, activation='relu'),  # 두 번째 Dense 레이어
    Dense(10, activation='softmax')  # 출력 레이어 (10개의 클래스)
])

# 모델 컴파일
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# 모델 학습
model.fit(x_train, y_train, epochs=10, batch_size=32, validation_split=0.2)

# 평가
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"테스트 손실: {test_loss}")
print(f"테스트 정확도: {test_acc}")

# 예측
predictions = model.predict(x_test[:5])
print("예측 결과:", predictions.argmax(axis=1))