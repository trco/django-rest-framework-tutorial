from django.contrib import admin
from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from . import views


app_name = 'tutorial_4'
urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<pk>', views.UserDetail.as_view()),

    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<pk>', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
