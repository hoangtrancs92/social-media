from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from .models import *
from django.core import serializers
from rest_framework import viewsets, permissions, generics, status
from rest_framework.views import APIView
from socialmedia.constant import TYPE_COMMENT, TYPE_LIKE
from .serializers import *
from rest_framework.authtoken.models import Token
from userApp.views import UserDetailAPIView, sen_email_report
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser
from django.db.models import Max
from django.db.models import Count
from datetime import datetime, timedelta
from django.db.models import Q
# Create your views here

    

# Dung CLASS VIEW.
class PostsViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] # Cho phép người dùng xem các Post
    
    def get_serializer_class(self):
        if self.action != 'list':
            return PostDetailSerializer
        return PostDetailSerializer
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated()] # yêu cầu xác thực để thực hiện các hành động này
        return super().get_permissions()
    
    def list(self, request):
        userId = request.query_params.get('userId')
        if userId is not None:
            user = CustomUser.objects.get(pk=userId)
            queryset = self.get_queryset().filter(status=True, user=user)
        else:
            if request.user.is_authenticated:
                queryset = self.get_queryset().filter(status=True).exclude(user=request.user)
            else:
                queryset = self.get_queryset().filter(status=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    def create(self, request, *args, **kwargs):
        try: 
            data = request.data
            user =  CustomUser.objects.get(pk=data['user'])
            post = Post.objects.create(
            title = data['title'],
            user = user,
            description = data['description'],
            status = True,
            urlImages=data['urlImages']
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
        except CustomUser.DoesNotExist: 
            return Response({'error':"The Post is not found with id:  {}".format(data['user'])}, status=status.HTTP_404_NOT_FOUND)  
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
    
    
    # @action(detail=False, methods=['get'], url_path='(my-post/?P<user_id>[^/.]+)')
    # def get_post_by_user_current(self, request, user_id=None):
    #     user = CustomUser.objects.get(pk=user_id)
    #     queryset = self.get_queryset().filter(user=user)
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)

    # detail=True-> áp dụng 1 post cụ thể, api/posts/{if}/method_name. detail=False api/posts/method_name
    @action(detail = True, methods=['get'])
    def discussions(self, request, pk = None): # pk là một tham số tùy số cho biết id của đối tượng cụ thể
         post = self.get_object()
         discussions = Discussion.objects.filter(post=post)
         serializer = DiscussionSerializerRetrieve(discussions,many=True)
         return Response(serializer.data)
    @action(detail = True, methods=['get'])
    def likes_discussions_counter(self, request, pk = None): # pk là một tham số tùy số cho biết id của đối tượng cụ thể
        post = self.get_object()
        count_comments = Discussion.objects.filter(post=post, type = TYPE_COMMENT).count() # Count Comment
        count_likes = Discussion.objects.filter(post=post, type =TYPE_LIKE ).count() # Count Comment
        return Response({'comment_number': count_comments, 'like_number':count_likes}, status=status.HTTP_200_OK)
    @action(detail=True, methods=['get'],url_path='auction-histories')
    def auction_history(self, request, pk = None):
        post = self.get_object()
        auction_histories = AuctionHistory.objects.filter(post=post)
        serializer = AuctionHistorySerializer(auction_histories,many=True)
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
    
    @action(detail = False, methods=['get'], url_path='(?P<name>[^/.]+)/posts', url_name='Get posts by the tag name')
    def posts(self, request, name=None):
        
        posts = Post.objects.filter(tags__name__icontains=name)
        serializer = PostSerializer(posts,many=True)
        return Response({'data':serializer.data}, status=status.HTTP_200_OK)
    def create(self, request, *args, **kwargs):
        name = request.data.get('name',None)
        if name: 
            tag, isCreated = Tag.objects.get_or_create(name=name)
            if not isCreated:
                serializer = self.get_serializer(tag)
                return Response(serializer.data, status= status.HTTP_201_CREATED)
            serializer = self.get_serializer(tag)
            return Response(serializer.data, status= status.HTTP_200_OK)
        return Response({'error': 'The name is required'}, status=400)
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

class AuctionHistoryViewSet(viewsets.ModelViewSet):
    serializer_class = AuctionHistorySerializer
    queryset = AuctionHistory.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] 

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated()]
        return super().get_permissions()
    
    def create(self, request, *args, **kwargs):
        data = request.data 

        try:
            user_id = data['user_id']
            user = CustomUser.objects.get(pk=user_id)

            author_id = data['author']
            author = CustomUser.objects.get(pk=user_id)

            post_id = data['post_id']
            post = Post.objects.get(pk=post_id)

            
            price = data['price']
            max_price_post_auction = post.auction_histories.aggregate(Max('price'))['price__max']
            if price < max_price_post_auction:
                return Response({'message':'The price must be greater than {}.'.format(max_price_post_auction)}, status=status.HTTP_400_BAD_REQUEST)
           
            # auctionSaved = AuctionHistory.objects.create(author=author,post=post,user_id=user_id,price) 
            return Response({'message':'The auction history created.'}, status=status.HTTP_201_CREATED)
        except Post.DoesNotExist:
            return Response({'message':'The post not found.'},status=status.HTTP_404_NOT_FOUND)
        except CustomUser.DoesNotExist:
            return Response({'message':'The user not found.'},status=status.HTTP_404_NOT_FOUND)

class AuctionHistoryViewSets(APIView):
    serializer_class = AuctionHistorySerializer
    queryset = AuctionHistory.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] 

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated()]
        return super().get_permissions()


    def create(self, request, *args, **kwargs):
        data = request.data 

        try:
            user_id = data['user_id']
            user = CustomUser.objects.get(pk=user_id)

            author_id = data['author']
            author = CustomUser.objects.get(pk=user_id)

            post_id = data['post_id']
            post = Post.objects.get(pk=post_id)
           
            # auctionSaved = AuctionHistory.objects.create(author=author,post=post,user_id=user_id,price=data['price']) 
            return Response({'message':'The auction history created.'}, status=status.HTTP_201_CREATED)
        except Post.DoesNotExist:
            return Response({'message':'The post not found.'},status=status.HTTP_404_NOT_FOUND)
        except CustomUser.DoesNotExist:
            return Response({'message':'The user not found.'},status=status.HTTP_404_NOT_FOUND)

class ReportCreateView(generics.CreateAPIView):
    serializer_class = ReportSerializer
    def post(self, request, *args, **kwargs):
        data = request.data 
        try:
            user = CustomUser.objects.get(pk=data['reporter'])
            post = Post.objects.get(pk=data['post_id'])
            report_text = data['report_text']
            report_saved = Report.objects.create(report_text= report_text, reporter=user, report_type=data['report_type'], reported_post=post)
            # Send Email Report
            sen_email_report(report_text, user.username)
            return Response({'message':'The report has been sent successfully.'}, status=status.HTTP_201_CREATED)
        except Post.DoesNotExist:
            return Response({'message':'The post not found.'},status=status.HTTP_404_NOT_FOUND)
        except CustomUser.DoesNotExist:
            return Response({'message':'The user not found.'},status=status.HTTP_404_NOT_FOUND)
class FileUploadView(generics.GenericAPIView):
    def post(self, request, format=None):
        file_obj = request.FILES['file']
        with open('media/' + file_obj.name, 'wb+') as destination:
            for chunk in file_obj.chunks():
                destination.write(chunk)
        file_path = 'api/media/' + file_obj.name
        return Response({'status': 'success','path':file_path})


# Statistics API
class PostStatisticsView(generics.RetrieveAPIView):
        def get(self, request, month,year):
            today = datetime.today()
            post_count = Post.objects.filter(Q(created_date__month=month) & Q(created_date__year=year)).aggregate(count=Count('id'))['count']
            return Response({'result':post_count}, status=status.HTTP_200_OK)