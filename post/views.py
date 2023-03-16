from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
from django.core import serializers
from rest_framework import viewsets, permissions, generics
from .serializers import *


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
    queryset = Post.objects.all()
    serializer_class = PostSerializer
class PostsList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = Tag