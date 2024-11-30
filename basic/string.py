# 문자열
my_str = "hello"
print(my_str)
print(type(my_str))

my_str = 'hello'
print(my_str)
print(type(my_str))

my_str = '''hello
world'''
print(my_str)
print(type(my_str))

my_str = """hello
world"""
print(my_str)
print(type(my_str))

# 문자열 포맷팅
my_str = 'My name is %s' % 'taeyang'
print(my_str)

my_str = '%d x %d = %d' % (2, 3, 2*3)
print(my_str)

my_str = '%f' % 3.14
print(my_str)

my_str = 'My name is {}'.format('taeyang')
print(my_str)

my_str = '{} x {} = {}'.format(2, 3, 2*3)
print(my_str)

# indexing
my_str = 'hello'
print(my_str[0])
print(my_str[4])
print(my_str[-1])

# slicing
my_str = 'hello'
print(my_str[1:3])

# split
my_str = 'hello world'
print(my_str.split())
my_str = 'hello,world'
print(my_str.split(','))

# DocString
"""이것도 주석입니다."""

# escape
# \n 줄바꿈, \t 탭, \\ 역슬래시, \' 작은 따옴표, \" 큰 따옴표
my_str = 'hello\nworld'
print(my_str)
print('집단지성', end='')
