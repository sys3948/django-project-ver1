from django.urls import path
from .views import BookmarkListView


urlpatterns = [
    path('', BookmarkListView.as_view(), name='list'), # 첫 번째 인자는 URL/ 다음의 내용, 두 번째 인자는 뷰함수 or 뷰 클래스로 클래스일 경우 as_view()를 사용해야한다. 세 번째 인자는 해당 name 값으로 URL 패턴을 찾을 수 있도록 하는 역활이다.
]