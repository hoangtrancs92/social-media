from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from .models import *
from django.core import serializers
from rest_framework import viewsets, permissions, generics, status
from .serializers import *
from rest_framework.authtoken.models import Token
from userApp.views import UserDetailAPIView


# Create your views here
# Dung HAM VIEW.
#Mọi view đều có tham số đầu tiên là request
def index(request):
    q = request.GET.get('q', '')# ?q=abcd
    return HttpResponse("The param Search is: {}".format(q))
    # return HttpResponse("Hello world")
def render(request):
    return render(request, template_name='index.html', context={
        'name':'Sang'
    })
    


def details(request,pk):
    try:
        postModel = Post.objects.get(pk=pk)
        return JsonResponse(serializers.serialize('json', postModel), content_type="application/json")
    except Post.DoesNotExist:
        return HttpResponse("The param pk is: {}".format(pk))   

# Dung CLASS VIEW.
class PostsViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] # Cho phép người dùng xem các Post
    
    def get_serializer_class(self):
        if self.action != 'list':
            return PostDetailSerializer
        return PostSerializer
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated()] # yêu cầu xác thực để thực hiện các hành động này
        return super().get_permissions()
    def create(self, request, *args, **kwargs):
        data = request.data
        post = Post.objects.create(
            title = data['title'],
            user = UserDetailAPIView.get_current_User(self,request),
            description = data['description'],
            status = True,
        )
        tags = data['tags']
        for tag in tags:
            tagAdded, isCreate = Tag.objects.get_or_create(name=tag['name'])
            post.tags.add(tagAdded)
            
        
        post.link = f"{request.build_absolute_uri('/')[:-1]}/api/posts/{post.id}"
        post.save()
        serializer = self.get_serializer(post)
        return Response(serializer.data, status= status.HTTP_201_CREATED)
    def update(self, request, *args, **kwargs):
        try:
            id = self.kwargs['pk']
            post = Post.objects.get(pk=id)
            data = request.data
            post.tags.clear() # Xóa tag cũ
            tags = request.data.get('tags', [])
            for tag in tags:
                tagAdded, isCreate = Tag.objects.get_or_create(name=tag['name'])
                post.tags.add(tagAdded)
            post.title = data['title'];
            post.description = data['description']
            post.save()
            serializer = self.get_serializer(post)
            return Response(serializer.data, status= status.HTTP_200_OK)
        except Post.DoesNotExist: 
            return Response({'error':"The Post is not found with id:  {}".format(id)}, status=status.HTTP_404_NOT_FOUND)  
    def destroy(self, request, *args, **kwargs):
       
        try:
            id = self.kwargs['pk']
            post = Post.objects.get(pk=id)
            user = self.request.user
            # Check user is Admin or user là user tạo bài post đó
            isAdmin = user.is_authenticated and user.is_staff
            if isAdmin == False:
                if user.id == post.user.id: 
                    post.status = False
                    post.save()
                    return Response("The Post id deleted success.", status= status.HTTP_200_OK)
            return Response({'error':"The user don't allow delete post"}, status=status.HTTP_403_FORBIDDEN)
        except Post.DoesNotExist:
            return Response({'error':"The Post is not found with id:  {}".format(id)}, status=status.HTTP_404_NOT_FOUND)  
class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] # Cho phép người dùng xem các tag
    # Cấu hình user authenticated mới được làm các action
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated()]
        return super().get_permissions()
    
    def create(self, request, *args, **kwargs):
        name = request.data.get('name',None)
        if name: 
            tag, isCreated = Tag.objects.get_or_create(name=name)
            if not isCreated:
                serializer = self.get_serializer(tag)
                return Response(serializer.data, status= status.HTTP_201_CREATED)
            serializer = self.get_serializer(tag)
            return Response(serializer.data, status= status.HTTP_200_OK)
        return Response({'error': 'name is required'}, status=400)
    # Chỉ cho admin xóa
    def get_permissions(self):
        if self.action == 'destroy':
            return [permissions.IsAdminUser()]
        return super().get_permissions()
        
