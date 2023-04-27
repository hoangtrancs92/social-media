"""socialmedia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include, re_path
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('tags',TagViewSet, basename='tags')
router.register('posts', PostsViewSet, basename='posts')
router.register('discussions', DiscussionViewSet, basename='discussions')
router.register('auction-histories', AuctionHistoryViewSet, basename='auction_histories')


# Nơi nhận request endpoints
urlpatterns = [
    # path('', views.index, name="index"),
    # path('index', views.render, name="render"),
    # path('<int:pk>/', views.details, name="View detail post"), #Xem chi tiet bai post
    # path('', include('router.urls')),
    path('', include(router.urls)),
    path('report/', ReportCreateView.as_view(), name='report'),
    path('upload/', FileUploadView.as_view(), name='file-upload'),
    re_path('statistics/posts/count/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', PostStatisticsView.as_view(), name='count-post-by-month-number')

]
