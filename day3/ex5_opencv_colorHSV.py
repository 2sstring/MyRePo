import cv2
import numpy as np

# 이미지 읽기
image = cv2.imread('Lenna.png')

# 이미지를 BGR에서 HSV 색 공간으로 변환
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# HSV 성분 분리
h, s, v = cv2.split(hsv_image)

# 각 성분 출력하기
print("Hue(H) 값:")
print(h)

print("\nSaturation(S) 값:")
print(s)

print("\nValue(V) 값:")
print(v)

# 결과 이미지 확인
cv2.imshow('Original Image', image)
cv2.imshow('HSV - Hue', h)
cv2.imshow('HSV - Saturation', s)
cv2.imshow('HSV - Value', v)

# 키보드 입력을 대기한 후 창 닫기
cv2.waitKey(0)
cv2.destroyAllWindows()