# Python Django

## 설치 과정 및 설명

1. Visual Studio Code, Git, Python 설치

   - Python 설치 시 path 설정 무조건 체크하기 (안하면 command not found 뜸)

2. 가상환경 만들기

   - 가상환경 만드는 이유 : 파이썬 응용 프로그램은 종종 표준 라이브러리의 일부로 제공되지 않는 패키지와 모듈을 사용하기 때문에 특정 버전 라이브러리가 필요할 수 있어서. 즉 파이썬 설치가 모든 응용 프로그램의 요구 사항을 충족시키는 것이 불가능 할 수도 있어서.

   - 때문에 가상환경을 설치하면 각각의 응용 프로그램이 버전이 달라 버전을 업그레이드 해도 다른 응용 프로그램 환경에 영향을 미치지 않게 됨.

   - ```bash
     python -m venv 가상환경 이름
     ```

     최신 버전의 파이썬을 설치함. 여러 버전의 파이썬이 설치돼 있는 경우 원하는 버전 선택 가능.

     존재하지 않으면 해당 이름의 디렉토리를 만들고 파이썬 인터프리터 사본, 표준 라이브러리가 들어있는 디렉토리를 만듦.

     일반적인 디렉토리 위치는 .venv이다. 이 이름은 보통 셸에서 숨겨져 있도록 하므로 디렉터리가 존재하는 이유를 설명하는 이름을 제공하면서도 방해받지 않는다. 또한 일부 툴링(tooling)이 지원하는 .env 환경 변수 정의 파일과의 충돌을 방지한다.

3. 가상환경 활성화

   - ```bash
     source 가상환경 이름/Scripts/activate
     ```

   - 보통 Tab키를 누르면 자동으로 입력됨.

   - 가상환경을 활성화하면 셸의 프롬프트가 변겨오디어 사용 중인 가상환경을 보여주고 환경을 수정하여 python을 실행하면 특정 버전의 파이썬이 실행된다.

4. pip로 패키지 관리하기

   - pip 프로그램 사용하여 패키지 설치, 업그레이드 및 제거 가능.

   - pip upgrade 해두기.

     ```bash
     python -m pip install --upgrade pip
     ```

   - ```bash
     pip search 패키지명
     pip install 패키지명==2.6.0 # 특정 버전 패키지 설치 가능
     pip uninstall 패키지명
     pip list # 패키지 리스트 표시  == pip freeze
     ```

   - 장고 설치

     ```bash
     pip install django
     pip list # django가 설치됐는지 확인.
     ```

5. vscode에 git 연동

   - vscode로 열려진 폴더에 git init 를 하면 저절로 연동 됨.
   - 터미널 열기 후 기본 셸 선택 후 bash 선택

## 프로젝트 및 앱 만들기

```bash
django-admin startproject 프로젝트이름
django-admin startapp 앱이름
python manage.py runserver # manage.py가 있는 경로에서 실행하면 server 실행됨.
```





