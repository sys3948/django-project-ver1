from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # path함수는 path(route, view, kwargs, name)인 형태로 호출하며 4개의 인수를 설명하면 route : 주소를 의미, view : route 인수로 접근했을 때 호출할 view, kwargs : view에 전달될 값들, name : route의 이름을 의미
    path('<int:question_id>/', views.detail, name='detail'), # <>의 의미는 변수를 의미한다. 이 부분에 해당하는 값을 뷰에 인자로 전달한다. views.detail에 questioni_id 인자로 해당 값이 들어간다.
    path('<int:question_id>/result/', views.result, name='result'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]