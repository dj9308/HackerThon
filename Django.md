# Django



## 설정

```bash
python -m venv venv
# 가상환경 실행
source ./venv/Scripts/activate
pip list

pip install django
django-admin startproject 이름

#앱 만들기
django-admin startapp 앱 이름

#서버 가동
python manage.py runserver
```

INSTALLED_APPS = [

​    '앱 이름', 으로 설정

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'



앱 이름 안에 templates 폴더 생성.(html파일들 넣는 장소)

```python
#views.py
def index(request):
    return HttpResponse('Welcome to Django')

#urls.py
from django.contrib import admin
from django.urls import path
# 앱이름 home 아래 views에서 가져옴ㅇㅇ
from home import views

urlpatterns = [
    path('home/square/<int:width>/<int:height>',views.square),
    path ('home/index/', views.index),
    path('admin/', admin.site.urls),
]


random.sample # 여러개 추출
random.sample # 하나 추출


def square(request,width,height):
    answer = width*height
    return render(request,'square.html',{'width':width,'height':height,'answer':answer})

```



## DB 설정

```bash
# 예제 프로젝트 및 앱 만들기
django-admin startproject django_blog
django-admin startapp articles
```

```PYTHON
# settings 한글 설정 후 앱 설정에 'articles' 입력

# models.py에 DB 클래스 설정
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) #최초 생성된 시간만 등록함
    updated_at = models.DateTimeField(auto_now=True) #수정될때 마다 시간이 변경
```

```bash
# DB올리기 전에 확인하는 작업
python manage.py makemigrations
pyhton manage.py migrate

python manage.py runserver

python manage.py shell
	from articles.models import Article   # 클래스 임포트
	Article.objects.all() # 객체 갯수 확인
	exit() # 나가기
	
	article = Article()  # 객체 생성
	article.title='first' # 데이터 입력
	article.content='django'
	
	article = Article(title='', content='')
	
	Article.objects.create(title='', content='')
	
	# 검색 방법
	Article.objects.filter(title='')
	Article.objects.filter(title='').last
	Article.objects.get(pk=1)
	#pk는 고유값이므로 해당 데이터가 지워져도 다시 나올수 없음.
	
	#업데이트
	Article = 검색한 데이터
	Article.변수명 = 바꿀 데이터 내용
	
	#삭제
	Article = 검색한 데이터
	Article.delete()
	Article.save()
```

- 테이블 확인 방법

  sqlite 설치 후 Ctrl + Shift + p 누르면 sqlite 창이 뜸. => open database 선택 => 익스플로러 창 맨 아래 sqlite explorer 안에 show table 클릭.

- Django 관리

  ```bash
  python manage.py createsuperuser
  # 이름, 메일(패스 가능), 비밀번호 설정
  # 이후 서버 실행후 /admin으로 들어간 후 로그인.
  ```

  ```python
  from django.contrib import admin
  from .models import Article
  
  class ArticleAdmin(admin.ModelAdmin):
      list_display = ('pk','title','content','created_at','updated_at')
  
  #테이블 형태로 표현시켜줌.
  admin.site.register(Article, ArticleAdmin)
  ```

- 자동으로 임포트해주는 방법

  ```bash
  pip install django-extensions
  python manage.py shell_plus
  
  article = Article()
  #자동으로 임포트 시켜준다.
  ```

## DB를 이용한 HTML 작성

- article 안에 urls.py 작성

  ```python
  #urls.py
  from django.urls import path
  from . import views
  
  urlpatterns= [
      path('create/',views.create),
      path('new/',views.new),
      path('',views.index),
  ]
  
  ```

  - templates 만든 후 안에 articles 폴더 작성.(그안에 html 파일들 만들거임.)