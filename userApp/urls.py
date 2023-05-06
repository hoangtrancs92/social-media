from django.urls import path
from .views import RegisterAPIView, UserDetailAPIView, RegisterAPIViewVersion1, UserEditAPIView, GetUserByIdAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('details', UserDetailAPIView.as_view(), name='view-details'),
    path('v1/register/', RegisterAPIViewVersion1.as_view(), name='user-register'),
    path('', UserEditAPIView.as_view(), name='user-register'),
    path ('<int:id>/', GetUserByIdAPIView.as_view(), name = 'get-user-detail-by-Id')
]