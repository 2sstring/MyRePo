import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt
import numpy as np

# 1. CIFAR-10 데이터셋 로드 및 전처리
(x_train, y_train), (x_test, y_test) = datasets.cifar10.load_data()

# 데이터 정규화 (0~255 -> 0~1)
x_train, x_test = x_train / 255.0, x_test / 255.0

# 클래스 이름 설정
class_names = ['Airplane', 'Automobile', 'Bird', 'Cat',
               'Deer', 'Dog', 'Frog', 'Horse', 'Ship', 'Truck']

# 2. 모델 생성
model = models.Sequential([

    # CNN Layer 1
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
    layers.MaxPooling2D((2, 2)),

    # CNN Layer 2
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),

    # CNN Layer 3
    layers.Conv2D(64, (3, 3), activation='relu'),

    # Flatten 및 Dense
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10)  # CIFAR-10 클래스 개수 = 10
])

# 3. 모델 컴파일
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# 모델 구조 요약 출력
model.summary()

# 4. 모델 학습
history = model.fit(x_train, y_train, epochs=10,
                    validation_data=(x_test, y_test))

# 5. 테스트 데이터로 예측
predictions = model.predict(x_test)


# 6. 시각적 출력
def plot_sample_predictions():
    plt.figure(figsize=(10, 10))
    for i in range(25):  # 25개의 샘플을 시각화
        idx = np.random.randint(0, len(x_test))  # 랜덤 샘플 선택
        plt.subplot(5, 5, i + 1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)

        # 이미지 데이터 및 실제 클래스
        plt.imshow(x_test[idx], cmap=plt.cm.binary)
        actual_label = class_names[y_test[idx][0]]

        # 예측 클래스
        predicted_label = class_names[np.argmax(predictions[idx])]
        color = 'blue' if actual_label == predicted_label else 'red'
        plt.xlabel(f"Actual: {actual_label}\nPredicted: {predicted_label}", color=color)

    plt.tight_layout()
    plt.show()


# 결과 시각화
plot_sample_predictions()