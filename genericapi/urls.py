from django.urls import path
from genericapi import views
urlpatterns=[
    path('articlelist',views.ArticleListView.as_view()),
    path('articlelistcreate',views.ArticleListCreateView.as_view()),
    path('articledetail/<int:pk>',views.ArticleDetailView.as_view()),
    path('articledetailupdate/<int:pk>',views.ArticleDetailUpdateView.as_view())
]