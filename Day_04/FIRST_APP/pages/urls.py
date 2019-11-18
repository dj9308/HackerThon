from django.urls import path
from . import views

app_name='pages'

urlpatterns = [
    path('',views.index),
    path('match/',views.match),
    path('home/',views.home),
    path('lotto/',views.lotto),
    path('cube/<int:num>/', views.cube),
    path('static_example/',views.static_example),
    # 앞의 경로로 갔을때 뒤 이름의 views로 이동하라.
]