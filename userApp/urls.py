from django.urls import path
from .views import RegisterAPIView, CustomAuthToken, UserDetailAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('details', UserDetailAPIView.as_view(), name='view-details')
]