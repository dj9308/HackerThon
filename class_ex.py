class Person:
    name = '아이유'

    def say_hello(self):
        print(f'hello! {self.name}')

# 클래스 -> 인스턴스
iu = Person()
#인스턴스를 통해 메서드를 호출
iu.say_hello()
#인스턴스를 통해 메서드를 호출
print(iu.name)
#클래스를 통해 속성에 접근
print(Person.name)
#클래스를 통해 메서드 호출
Person.say_hello

# class Person:
#     name = '아이유'
#     age = '19'

#     def greeting(self):
#         print(f'안녕하세요 저는 {self.name}입니다.')

# iu = Person()

word = "Not class member"

class Something:
    word = "Class member"

    def Set(self, msg):
        self.word = msg
    def Print(self):
        print(word)

g = Something()
g.Set('First Message')
g.Print()

class Person:
    def __init__(self, name):
        print(f'하이 {name}')
    def __del__(self):
        print('바이')
hong = Person('hong')

class Myclass:
    name = '홍길동'
    def __init__(self, value):
        self.value = value
        print(f'{self.value}가 생성되었습니다.')
    def __del__(self):
        print('소멸되었습니다.')

def foo():
    d = Myclass(10)
    foo()

class Person:
    def __init__(self,name):
        self.name = name

    def greeting(self):
        print(f'안녕하세요 저는 {self.name}입니다.')

class Student(Person):
    def __init__(self,name,student_id):
        self.name = name
        self.student_id = student_id
    def greeting(self):
        print(f'안녕하세요 저는 {self.name}입니다. 제 학번은 {self.student_id}입니다.')

s1 = Person('juan')
s1.greeting()
s2 = Student('justin',12345)
s2.greeting()

