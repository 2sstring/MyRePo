import cv2
import numpy as np

# 이미지를 읽습니다.
image = cv2.imread('candies.png')

# 이미지를 BGR 채널로 분리합니다.
b_channel, g_channel, r_channel = cv2.split(image)

# 빨간색(R) 성분이 50 이상인 마스크를 만듭니다.
red_mask = cv2.inRange(r_channel, 200, 255)

# 마스크를 기반으로 원본 이미지에서 해당 부분만 추출합니다.
result = cv2.bitwise_and(image, image, mask=red_mask)

# 결과 이미지를 출력합니다.
cv2.imshow("Original Image", image)
cv2.imshow("Red Mask", red_mask)
cv2.imshow("Red Filtered Image", result)

# 사용자가 아무 키나 누를 때까지 창 유지
cv2.waitKey(0)
cv2.destroyAllWindows()