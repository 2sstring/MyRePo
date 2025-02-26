import cv2

# 카메라 초기화 (0은 기본 카메라를 의미)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("카메라를 열 수 없습니다.")
    exit()

while True:
    # 카메라에서 프레임 읽기
    ret, frame = cap.read()
    if not ret:
        print("프레임을 읽을 수 없습니다. 프로그램을 종료합니다.")
        break

    # 프레임 출력
    cv2.imshow("Camera Output", frame)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 모든 자원 해제
cap.release()
cv2.destroyAllWindows()