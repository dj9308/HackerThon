import requests
import random

area_code = {
    '서울':'02'
}
area_code['경기도']='031'

# print(area_code)

'''
Python dictionary 연습 문제
'''

# 1. 평균을 구하시오.
score = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}

# 아래에 코드를 작성해 주세요.
# print('==== Q1 ====')
print(sum(score.values)/len(score))
# 2. 반 평균을 구하시오. -> 전체 평균
scores = {
    'a': {
        '수학': 84,
        '국어': 90,
        '음악': 92
    },
    'b': {
        '수학': 83,
        '국어': 91,
        '음악': 77
    }
}

# 아래에 코드를 작성해 주세요.
# print('==== Q2 ====')

a_total = 0
b_total =0
for i in score['a']:
    a_total += scores['a'][i]
    a_ave = a_total/len(scores['a'])
print(a_ave)

# 3. 도시별 최근 3일의 온도입니다.
city = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

# 3-1. 도시별 최근 3일의 온도 평균은?
for i in city:
    total =0
    for j in range(len(city[i])):
        total += city[i][j]
    ave = total/len(city[i])
    print(f'{i}의 평균기온 : {round(ave,2)}도')

# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?
cnt = 0
for key, value in city.items():
    if cnt == 0:
        hot = max(value)
        cold = min(value)
        hot_city = key
        cold_city = key
    else:
        if hot < max(value):
            hot = max(value)
            hot_city = key
        if cold > min(value):
            cold = min(value)
            cold_city = key
    cnt += 1
print(hot_city)
print(cold_city)

# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?
if 2 in city['서울']:
    print['ㅇㅇ']
else:
    print['ㄴㄴ']

# 아래에 코드를 작성해 주세요.

elements= ['사랑','노안','집중력','운','돈','성욕']
words = ['을 적당히~','도 적당.. 엌ㅋ.. 쏟았넿ㅎㅎ', '는 언제 넣었는지 모르지만 충분하군!','을 실수한 척하고 다 털어넣자 ㅎㅎ']
random = random.sample(elements,3)+random.sample(words,3)
print(random)