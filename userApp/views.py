from rest_framework import status, authentication, generics, permissions, parsers
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CustomUser
from .serializer import UserSerializer
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import *
from django.core.mail import EmailMultiAlternatives
from socialmedia import constant
from rest_framework.parsers import MultiPartParser, FormParser
from django.http import FileResponse, Http404
from django.conf import settings
import os
from oauth2_provider.views import TokenView
from oauth2_provider.models import AccessToken

from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.authentication import JWTAuthentication


class RegisterAPIView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = CustomUser.objects.create_user(**serializer.validated_data)
            # send_email_register_success(user.email,user.username)
            return Response({'status': 'success', 'message': 'The user %s register successfully' %(user.username)}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegisterAPIViewVersion1(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        # Save the user and avatar image file
        serializer.save(avatar=self.request.data.get('avatar'))

    
class UserDetailAPIView(generics.RetrieveAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer
    def get_queryset(self):
        return CustomUser.objects.all()

    def get_object(self):
        user = self.request.user
        return user
class UserEditAPIView(generics.UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser, FormParser]

    def get_object(self):
        return self.request.user
    def perform_update(self, serializer):
        serializer.save(avatar=self.request.data.get('avatar'))

def send_email_register_success(emailTo, username):
    title = 'Thanks for Registering for the Social Media'
    body = '''<p>Dear <b>{username}</b>,</p>
    <p>Thanks for register for Social Media! We are looking forward to seeing you there and sharing our inbound marketing with you.</p>
    <p>Best,</p>
    Social Media Team
    '''.format(username = username)
    email_to = emailTo
    send_mail(constant.EMAIL_FROM,email_to,body,title)
def send_mail(emailFrom,emailTo,bodyStr,title):
    subject = title
    from_email = emailFrom
    to_email = emailTo
    body = bodyStr
    msg = EmailMultiAlternatives(subject,body,from_email,[to_email])  
    msg.attach_alternative(body, "text/html") # Set html
    msg.send()

def sen_email_report(report_text, username):
    title = 'Report'
    body = '''<p>Dear Admin,</p>
    <p>The user {username} has been report with content: <i>{report_text}</i></p>
    <p>Best,</p>
    Social Media Team
    '''.format(username = username, report_text = report_text)
    msg = EmailMultiAlternatives(title,body,constant.EMAIL_FROM,[constant.EMAIL_FROM])  
    msg.attach_alternative(body, "text/html") # Set html
    msg.send()
# THIS API TO GET IMAGE CONTENT
def get_avatar(request, filename):
    # Construct the file path for the requested avatar
    file_path = os.path.join(settings.MEDIA_ROOT, filename)
    # Check if the file exists
    if not os.path.exists(file_path):
        raise Http404
    # Open the file in binary mode and return a FileResponse object
    file = open(file_path, 'rb')
    response = FileResponse(file, content_type='image/png')
    return response