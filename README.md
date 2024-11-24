# Python 학습 자료

## Python 기초

### 변수
- **정의**: 변수를 사용하여 데이터를 저장합니다.
- **문법**: `변수명 = 값`
- **예제**:
    ```python
    x = 5
    name = "John"
    ```

### 데이터 타입
- **주요 데이터 타입**:
  - `int`: 정수
  - `float`: 실수
  - `str`: 문자열
  - `bool`: 불리언
  - `list`: 리스트
  - `tuple`: 튜플
  - `dict`: 딕셔너리
  - `set`: 집합

### 제어 구조
- **If 문**:
    ```python
    if 조건:
        # 코드 블록
    elif 다른_조건:
        # 다른 코드 블록
    else:
        # 다른 코드 블록
    ```
- **For 문**:
    ```python
    for 항목 in 반복가능한_객체:
        # 코드 블록
    ```
- **While 문**:
    ```python
    while 조건:
        # 코드 블록
    ```

### 함수
- **정의**: 함수는 특정 작업을 수행하는 코드 블록입니다.
- **문법**:
    ```python
    def 함수명(매개변수):
        # 코드 블록
        return 값
    ```
- **예제**:
    ```python
    def add(a, b):
        return a + b
    ```

## Python 중급

### 리스트 내포
- **정의**: 리스트를 생성하는 간결한 방법입니다.
- **문법**:
    ```python
    [표현식 for 항목 in 반복가능한_객체 if 조건]
    ```
- **예제**:
    ```python
    squares = [x**2 for x in range(10)]
    ```

### 람다 함수
- **정의**: `lambda` 키워드로 정의된 익명 함수입니다.
- **문법**:
    ```python
    lambda 인자: 표현식
    ```
- **예제**:
    ```python
    add = lambda x, y: x + y
    ```

### 모듈과 패키지
- **모듈 임포트**:
    ```python
    import 모듈명
    from 모듈명 import 함수명
    ```
- **예제**:
    ```python
    import math
    from math import sqrt
    ```

### 예외 처리
- **Try-Except 블록**:
    ```python
    try:
        # 코드 블록
    except 예외타입 as e:
        # 예외 처리 코드
    finally:
        # 항상 실행되는 코드 블록
    ```

### 파일 입출력
- **파일 읽기**:
    ```python
    with open('file.txt', 'r') as file:
        content = file.read()
    ```
- **파일 쓰기**:
    ```python
    with open('file.txt', 'w') as file:
        file.write('Hello, World!')
    ```

### 클래스와 객체
- **클래스 정의**:
    ```python
    class 클래스명:
        def __init__(self, 속성):
            self.속성 = 속성

        def 메서드(self):
            # 코드 블록
    ```
- **예제**:
    ```python
    class Dog:
        def __init__(self, name):
            self.name = name

        def bark(self):
            print(f"{self.name} says woof!")
    ```

## Python 고급

### 데코레이터
- **정의**: 함수를 수정하지 않고 기능을 추가하는 방법입니다.
- **문법**:
    ```python
    def 데코레이터(함수):
        def 래퍼(*args, **kwargs):
            # 추가 기능
            return 함수(*args, **kwargs)
        return 래퍼
    ```
- **예제**:
    ```python
    def my_decorator(func):
        def wrapper():
            print("Something is happening before the function is called.")
            func()
            print("Something is happening after the function is called.")
        return wrapper

    @my_decorator
    def say_hello():
        print("Hello!")
    ```

### 제너레이터
- **정의**: 이터레이터를 생성하는 함수입니다.
- **문법**:
    ```python
    def 제너레이터():
        yield 값
    ```
- **예제**:
    ```python
    def count_up_to(max):
        count = 1
        while count <= max:
            yield count
            count += 1
    ```

### 컨텍스트 매니저
- **정의**: 리소스를 자동으로 관리하는 방법입니다.
- **문법**:
    ```python
    with 표현식 as 변수:
        # 코드 블록
    ```
- **예제**:
    ```python
    with open('file.txt', 'r') as file:
        content = file.read()
    ```

### 메타 클래스
- **정의**: 클래스의 동작을 제어하는 클래스입니다.
- **문법**:
    ```python
    class 메타클래스(type):
        def __new__(cls, name, bases, dct):
            # 클래스 생성 로직
            return super().__new__(cls, name, bases, dct)
    ```
- **예제**:
    ```python
    class MyMeta(type):
        def __new__(cls, name, bases, dct):
            print(f"Creating class {name}")
            return super().__new__(cls, name, bases, dct)

    class MyClass(metaclass=MyMeta):
        pass
    ```

이 문서는 Python의 기초, 중급 및 고급 기술에 대한 간략한 개요를 제공합니다. 자세한 내용은 공식 Python 문서를 참조하십시오.