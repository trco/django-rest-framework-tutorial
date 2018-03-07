from django.contrib import admin
from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from . import views

# using app_name namespace returned "Could not resolve URL for hyperlinked
# relationship using view name "user-detail". You may have failed to include the
# related model in your API, or incorrectly configured the `lookup_field`
# attribute on this field."

# app_name = 'tutorial_5'
urlpatterns = [

    path('api-entry/', views.api_root),

    path('users/',
         views.UserList.as_view(),
         name='user-list'),
    path('users/<pk>',
         views.UserDetail.as_view(),
         name='user-detail'),

    path('snippets/',
         views.SnippetList.as_view(),
         name='snippet-list'),
    path('snippets/<pk>',
         views.SnippetDetail.as_view(),
         name='snippet-detail'),
    path('snippets/<pk>/highlight/',
         views.SnippetHighlight.as_view(),
         name='snippet-highlight'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
