from django.urls import path
from .views import BookmarkListView, BookmarkCreateView, BookmarkDetailView, BookmarkUpdateView, BookmarkDeleteView


urlpatterns = [
    path('', BookmarkListView.as_view(), name='list'), # 첫 번째 인자는 URL/ 다음의 내용, 두 번째 인자는 뷰함수 or 뷰 클래스로 클래스일 경우 as_view()를 사용해야한다. 세 번째 인자는 해당 name 값으로 URL 패턴을 찾을 수 있도록 하는 역활이다.
    path('add/', BookmarkCreateView.as_view(), name='add'),
    path('detail/<int:pk>', BookmarkDetailView.as_view(), name='detail'),
    path('update/<int:pk>', BookmarkUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', BookmarkDeleteView.as_view(), name='delete'),
]