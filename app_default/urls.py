from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # path함수는 path(route, view, kwargs, name)인 형태로 호출하며 4개의 인수를 설명하면 route : 주소를 의미, view : route 인수로 접근했을 때 호출할 view, kwargs : view에 전달될 값들, name : route의 이름을 의미
]