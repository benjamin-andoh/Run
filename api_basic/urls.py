from .views import article_list, article_details, ArticleDetails, ArticleAPIView, GenericAPIView
from django.urls import path

urlpatterns = [

    path('list', article_list),
    path('details/<pk>', article_details),

    path('articlecreate', ArticleAPIView.as_view()),
    path('articledetails/<int:id>', ArticleDetails.as_view()),

    path('generic/article/<int:id>', GenericAPIView.as_view()),

]
