"""movieapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include
from movieapi.app import views

"""
TODO:
- Comment
- Add all the views
"""

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.api_root),

    path('reviews/',
        views.ReviewList.as_view(),
        name='review-list'),
    path('reviews/<int:pk>',
        views.ReviewDetail.as_view(),
        name='review-detail'),

    path('comments/',
        views.CommentList.as_view(),
        name='comment-list'),
    path('comments/<int:pk>',
        views.CommentDetail.as_view(),
        name='comment-detail'),

    path('movies/',
        views.MovieList.as_view(),
        name='movie-list'),
    path('movies/<int:pk>',
        views.MovieDetail.as_view(),
        name='movie-detail'),

    path('actors/',
        views.ActorList.as_view(),
        name='actor-list'),
    path('actors/<int:pk>',
        views.ActorDetail.as_view(),
        name='actor-detail'),

    path('movieactors/',
        views.MovieActorList.as_view(),
        name='movieactor-list'),
    path('movieactors/<int:pk>',
        views.MovieActorDetail.as_view(),
        name='movieactor-detail'),

    path('trailers/',
        views.TrailerList.as_view(),
        name='trailer-list'),
    path('trailers/<int:pk>',
        views.TrailerDetail.as_view(),
        name='trailer-detail'),

    path('categories/',
        views.CategoryList.as_view(),
        name='category-list'),
    path('categories/<int:pk>',
        views.CategoryDetail.as_view(),
        name='category-detail'),

    path('moviecategories/',
        views.MovieCategoryList.as_view(),
        name='moviecategory-list'),
    path('moviecategories/<int:pk>',
        views.MovieCategoryDetail.as_view(),
        name='moviecategory-detail'),

    path('users/',
        views.UserList.as_view(),
        name='user-list'),
    path('users/<int:pk>/',
        views.UserDetail.as_view(),
        name='user-detail'),

    path('groups/',
        views.GroupList.as_view(),
        name='group-list'),
    path('groups/<int:pk>/',
        views.GroupDetail.as_view(),
        name='group-detail'),
        
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)