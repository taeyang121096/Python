# 리스트 mutable
# 리스트는 여러 데이터를 하나로 묶어서 관리할 수 있는 자료형
# 리스트는 대괄호([])로 묶어서 표현하며, 각 요소는 쉼표(,)로 구분
# 리스트에 저장된 요소는 인덱스를 이용해 접근
# 리스트에 저장된 요소는 변경 가능
# 리스트에 저장된 요소는 다양한 자료형을 혼합하여 사용 가능
# 리스트에 저장된 요소는 다른 리스트를 포함할 수 있음

my_list = []
print(my_list)
print(type(my_list))

my_list.append(1)


my_list.append(6)
my_list.append(5)

print(my_list)

print(my_list[0])

# 리스트 요소 변경
del my_list[0]

my_list.append(3)
print(my_list)

# 리스트 슬라이싱
print(my_list[0:2])

print(my_list)
my_list.sort()

print(my_list)
print(my_list.count(3))

print(len(my_list))