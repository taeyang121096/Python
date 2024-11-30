# 숫자 정수, 실수
my_int = 3
my_float = 3.2

# type() 함수는 변수의 데이터 타입을 반환한다.
type(my_float)
type(my_int)

# 문자열 작은 따옴표, 큰 따옴표 가능
my_string = 'hello'
my_string2 = "hello"

# boolean 참, 거짓
my_bool = True
my_bool2 = False

# List 자료형
my_list = [1, 2, 3]
my_list2 = ['hello', 'world']
for i in my_list2:
    print(i)
my_list2.append('test')
my_list2[0] = 'test'

# Tuple 자료형
my_tuple = (1, 2, 3)

# Dictionary 자료형
my_dict = {'name': 'taeyang', 'age': 29}

# Set 자료형
my_set = {1, 2, 3}

# 자료형 변경
my_int = str(my_int)
my_float = int(my_float)
my_string = list(my_string)