# 구구단 출력 함수
def print_gugudan():
    for i in range(2, 10):  # 2단부터 9단까지
        print(f"=== {i}단 ===")
        for j in range(1, 10):  # 곱해지는 숫자
            print(f"{i} x {j} = {i * j}")
        print()  # 단 간격 띄우기


# 구구단 실행
if __name__ == "__main__":
    print_gugudan()