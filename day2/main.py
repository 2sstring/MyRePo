if __name__ == '__main__':
    a = 5
    b = 10
    print(a + b)# 사칙연산 함수들
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    # Division by zero 방지
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y

def power(a, b):
    return a ** b

def mod(a, b):
    return a % b


# 테스트 코드
if __name__ == "__main__":
    # 테스트 값
    a = 10
    b = 5

    print("Add:", add(a, b))  # 10 + 5 = 15
    print("Subtract:", subtract(a, b))  # 10 - 5 = 5
    print("Multiply:", multiply(a, b))  # 10 * 5 = 50
    print("Divide:", divide(a, b))  # 10 / 5 = 2.0
    print("f*{X} ** f*{y} = ", power(a, b) )
    print("f*{X} % f*{y} = ", mod(a, b))

    # Division by zero 테스트
    b = 0
    print("Divide by zero:", divide(a, b))  # 에러 처리