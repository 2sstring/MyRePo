import cv2

# 동영상 파일 경로
video_path = "test_video.mp4"

# VideoCapture 객체 생성
cap = cv2.VideoCapture(video_path)

# 동영상 파일이 열리지 않으면 오류 메시지 출력
if not cap.isOpened():
    print("Error: 동영상을 열 수 없습니다.")
    exit()

# 프레임 반복 읽기
while True:
    # 한 프레임 읽기
    ret, frame = cap.read()

    # 프레임을 정상적으로 읽지 못한 경우 (예: 동영상 끝)
    if not ret:
        print("동영상 재생이 끝났거나 문제가 발생했습니다.")
        break

    # 프레임 출력
    cv2.imshow('Video Playback', frame)

    # 'q' 키를 눌러 동영상 재생 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 자원 해제
cap.release()
cv2.destroyAllWindows()