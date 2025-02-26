import cv2
import numpy as np

# 이미지 읽기 (이미지 파일 경로를 사용하세요)
image = cv2.imread('mountain.jpg', cv2.IMREAD_GRAYSCALE)  # 색상 이미지를 읽기
if image is None:
    print("이미지를 찾을 수 없습니다. 경로를 확인해주세요.")
    exit()

# 1. 평균값 필터 적용
average_filter = cv2.blur(image, (5, 5))  # 5x5 커널 크기 사용

# 2. 샤프닝 필터 적용
# 샤프닝 커널 정의
sharpen_kernel = np.array([[0, -1, 0],
                           [-1, 5, -1],
                           [0, -1, 0]])
sharpened_image = cv2.filter2D(image, -1, sharpen_kernel)

# 3. 라플라시안 필터 적용
laplacian_image = cv2.Laplacian(image, cv2.CV_64F)  # CV_64F는 실수형 데이터 타입

# 결과 출력
cv2.imshow('Original Image', image)
cv2.imshow('Average Filter', average_filter)
cv2.imshow('Sharpening Filter', sharpened_image)
cv2.imshow('Laplacian Filter', cv2.convertScaleAbs(laplacian_image))  # 절대값 변환 후 출력

# 키 입력 대기 및 창 닫기
cv2.waitKey(0)
cv2.destroyAllWindows()