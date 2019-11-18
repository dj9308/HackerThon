# 함수의 종류
#1. 인자 & 리턴 O
def sum_ex(a,b):
    result = a+b
    return result

print(sum_ex(2,5))
sum_result = sum_ex(2,5)
print(sum_result)

#2. 리턴만
def say():
    return 'hi'
print(say())

#3. 인자만
def say(name, age):
    print(f'제 이름은 {name}이고, 나이는 {age}입니다.')
say('juan',20)

#4. 인자 & 리턴 X
def say():
    print('안녕하세요')

def say():
    print('hi')
say()
result = say()
print(result)

# 함수의 인자
#1. 위치 인자(Positional Argument)

def my_func(a,b,c):
    print(f'첫번째는 {a}, 두번째는 {b}, 세번째는 {c}입니다.')
    return a + b + c
result = my_func(1,2,3)
print(result)

#2. 기본값 인자(default argument)
def greeting(name = 'juan'):
    print(f'{name}님 안녕하세요')

# greeting()
# greeting('bob')

def my_sum(a,b=3):  #기본값 인자는 위치 인자 뒤에 있어야함
    return a+b

# print(my_sum(2))

print(my_sum(2))

def greeting(age, name='juan'):
    print(f'{name}은 {age}살 입니다.')

greeting(19,'faker')

greeting(name='john', age=33)  #순서 상관 음슴

#4. 가변인자
def my_func(*args):
    print(args)
    print(type(args))
    return args
my_func(1,2,3)
my_func(1,2,3,4)
my_func(1,2,3,5,6)

#5. 정의되지 않은 인자(키워드 인자)

def my_dict(**kwargs):
    print(kwargs)
    print(type(kwargs))

my_dict(한국어='안녕',영어='hi',독일어='Guten tag')

my_dict = {
    '서울':'02'
}

jumin1 = '900101-1020201'
jumin2 = '900101-2020201'

def male_female(number):
    if number[7] == '1':
        print('남자')
    else:
        print('여자')

male_female(jumin1)
male_female(jumin2)

#2. 사용자의 입력으로 숫자를 받아서 해당 숫자가 짝수,홀수를 구분하는 함수
def ques(number):
    if number%2==0:
        print('짝수')
    else:
        print('홀수')

ques(1)

# 리스트 안에서 가장 작은 숫자를 출력하는 함수
items = [1,2,-5,0]

def ques2(aa):
    print(min(aa))

ques2(items)

words = ['level','asder','tomato','abdeda','s']
cnt =0
def ques3(array):
    for i in len(array):
        if len(array[i])>2:
            if array[i][0] == array[i][-1:]:
                cnt+=1

print(cnt)

import requests
from bs4 import BeautifulSoup as bs
url = 'https://finance.naver.com/marketindex/'

html = requests.get(url).text
soup = bs(html,'html.parser')
select = soup.select_one('#exchangeList > li.on > ')
print(select.text)