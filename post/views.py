from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from .models import *
from django.core import serializers
from rest_framework import viewsets, permissions, generics, status
from .serializers import *
from rest_framework.authtoken.models import Token
from userApp.views import UserDetailAPIView
from rest_framework.decorators import action


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
            
        # Tạo link
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
    
    # detail=True-> áp dụng 1 post cụ thể, api/posts/{if}/method_name. detail=False api/posts/method_name
    @action(detail = True, methods=['get'])
    def discussions(self, request, pk = None): # pk là một tham số tùy số cho biết id của đối tượng cụ thể
         post = self.get_object()
         discussions = Discussion.objects.filter(post=post)
         serializer = DiscussionSerializer(discussions,many=True)
         return Response(serializer.data)
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
        
class DiscussionViewSet(viewsets.ModelViewSet):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        discussion_children = Discussion.objects.filter(parent_id=instance.id)
        while discussion_children.exists():
            discussion_children.delete()
            discussion_children = Discussion.objects.filter(parent_id=instance.id)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)