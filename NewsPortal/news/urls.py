from django.urls import path
from .views import ArticleList, ArticleDetail, ArticlePost, ArticleUpdateView, ArticleDeleteView, SearchArticleList

urlpatterns = [
    path('', ArticleList.as_view()),
    path('<int:pk>', ArticleDetail.as_view ()),
    path('add/', ArticlePost.as_view(), name='add'),
    path('update/<int:pk>', ArticleUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', ArticleDeleteView.as_view(), name='delete'),
    path('search/', SearchArticleList.as_view(), name='search'),
]