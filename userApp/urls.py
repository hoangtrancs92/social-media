from django.urls import path
from .views import RegisterAPIView, UserDetailAPIView, RegisterAPIViewVersion1, UserEditAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('details', UserDetailAPIView.as_view(), name='view-details'),
    path('api/v1/register/', RegisterAPIViewVersion1.as_view(), name='user-register'),
    path('api/users/', UserEditAPIView.as_view(), name='user-register'),
]