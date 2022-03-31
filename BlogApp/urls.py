from django.urls import path
from BlogApp import views


urlpatterns=[
    path('/blog',views.blogApi),
    path('/blog/([0-9]+)$',views.blogApi)
]
