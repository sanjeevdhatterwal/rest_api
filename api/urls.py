from django.urls import path
from api import views
urlpatterns=[
    path('user',views.userdata),
    path('articles',views.articleApi),
    path('createarticle',views.createArticleApi)
]