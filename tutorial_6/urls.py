from django.conf.urls import url, include
from django.urls import path

from rest_framework.routers import DefaultRouter
from . import views


# Router is used to automatically create urls for ViewSets
router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'snippets', views.SnippetViewSet)

# The API URLs are now determined automatically by the router.
# The DefaultRouter class also automatically creates the API root view and
# corresponding URL.
urlpatterns = [
    path('', include(router.urls))
]


"""from django.contrib import admin
from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers

from .views import UserViewSet, SnippetViewSet, api_root

# using app_name namespace returned "Could not resolve URL for hyperlinked
# relationship using view name "user-detail". You may have failed to include the
# related model in your API, or incorrectly configured the `lookup_field`
# attribute on this field."

# app_name = 'tutorial_6'

# Multiple views from each ViewSet class are created by binding the http methods
# to the required action for each view
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})
snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
snippet_detail = UserViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])


urlpatterns = [

    path('api-entry/', api_root),

    path('users/',
         user_list,
         name='user-list'),
    path('users/<pk>',
         user_detail,
         name='user-detail'),

    path('snippets/',
         snippet_list,
         name='snippet-list'),
    path('snippets/<pk>',
         snippet_detail,
         name='snippet-detail'),
    path('snippets/<pk>/highlight/',
         snippet_highlight,
         name='snippet-highlight'),
]

urlpatterns = format_suffix_patterns(urlpatterns)"""
