import cv2
import numpy as np

# 이미지 읽기
image = cv2.imread("candies.png")

# BGR 이미지를 HSV로 변환
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 붉은색의 HSV 범위 정의 (2개의 범위 사용, 왜냐하면 HSV는 원형으로 구성됨)
lower_red1 = np.array([0, 120, 70])    # 첫 번째 범위 (0° ~ 10°)
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 120, 70])  # 두 번째 범위 (170° ~ 180°)
upper_red2 = np.array([180, 255, 255])

# 두 영역의 마스크 생성
mask1 = cv2.inRange(hsv_image, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv_image, lower_red2, upper_red2)

# 두 영역의 마스크를 결합
red_mask = mask1 | mask2

# 원본 이미지에서 붉은색만 추출
red_extracted = cv2.bitwise_and(image, image, mask=red_mask)

# 결과 출력
cv2.imshow("Original Image", image)
cv2.imshow("Red Extracted", red_extracted)

# 키 입력 대기 후 종료
cv2.waitKey(0)
cv2.destroy