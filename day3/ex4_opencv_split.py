import cv2

# Lenna.png 파일 읽기
image = cv2.imread("Lenna.png")

# 이미지를 BGR 채널로 분리
b, g, r = cv2.split(image)

# 각 채널 출력
print("Blue Channel:\n", b)
print("\nGreen Channel:\n", g)
print("\nRed Channel:\n", r)

# 분리된 채널들을 시각화 (선택적으로)
cv2.imshow("Blue Channel", b)
cv2.imshow("Green Channel", g)
cv2.imshow("Red Channel", r)

cv2.waitKey(0)
cv2.destroyAllWindows()