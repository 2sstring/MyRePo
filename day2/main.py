def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    # Division by zero 방지
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b


def power(a, b):
    return a ** b


def mod(a, b):
    return a % b


# 테스트 코드
if __name__ == "__main__":
    # 테스트 값
    x = 10
    y = 5
    print("Add:", add(x, y))  # 10 + 5 = 15
    print("Subtract:", subtract(x, y))  # 10 - 5 = 5
    print("Multiply:", multiply(x, y))  # 10 * 5 = 50
    print("Divide:", divide(x, y))  # 10 / 5 = 2.0
    print("f*{X} ** f*{y} = ", power(x, y))
    print("f*{X} % f*{y} = ", mod(x, y))
    # Division by zero 테스트
    y = 0
    print("Divide by zero:", divide(x, y))  # 에러 처리# 상수
DIVIDE_BY_ZERO_ERROR = "Error: Cannot divide by zero"


# 산술 함수 정의
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return DIVIDE_BY_ZERO_ERROR
    return a / b


def power_of(a, b):
    return a ** b


def modulus(a, b):
    return a % b


# 테스트 코드
if __name__ == "__main__":
    # 테스트 값
    x, y = 10, 5

    # 연산 및 출력
    print(f"Add: {add(x, y)}")  # 10 + 5 = 15
    print(f"Subtract: {subtract(x, y)}")  # 10 - 5 = 5
    print(f"Multiply: {multiply(x, y)}")  # 10 * 5 = 50
    print(f"Divide: {divide(x, y)}")  # 10 / 5 = 2.0
    print(f"Power: {power_of(x, y)}")  # 10 ** 5 = 100000
    print(f"Modulus: {modulus(x, y)}")  # 10 % 5 = 0

    # Division by zero 테스트
    y = 0
    print(f"Divide by zero: {divide(x, y)}")  # 에러 처리