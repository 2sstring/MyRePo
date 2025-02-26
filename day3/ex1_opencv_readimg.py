import cv2

# 이미지를 읽기
image = cv2.imread('Lenna.png', cv2.IMREAD_GRAYSCALE)

# 이미지가 제대로 읽혔는지 확인
if image is None:
    print("이미지를 읽을 수 없습니다. 경로를 확인하세요.")
else:
    # 이미지를 출력
    cv2.imshow("Lenna", image)

    # 키 입력을 기다리고 창 닫기
    cv2.waitKey(0)
    cv2.destroyAllWindows()