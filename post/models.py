from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from userApp.models import CustomUser
from socialmedia.constant import STATUS_PENDING, NOT_STANDARD
class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True) #Tự động lấy thời điển hiện tại để thêm vào
    modified_date = models.DateTimeField(auto_now=True) # Khi có sự cập nhật sẽ tự động update lại
    status = models.BooleanField(default=True)

    class Meta:
        abstract = True

# Create Post model
class Post(BaseModel):
    title = models.CharField(null=False, max_length=100)
    description = models.TextField()
    link = models.CharField(null=False, max_length=255, blank=True)
    user = models.ForeignKey(CustomUser, on_delete= models.CASCADE) #Khi xóa user thì các bài post xóa hết
    tags = models.ManyToManyField('Tag',related_name='posts', null=True,blank=True) # Cho phep null, blank
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_date']
#Create Tag Model
class Tag(BaseModel):
    name = models.CharField(max_length=50, unique=True)
    class Meta:
        ordering = ['-created_date'] # '-'->DESC
    def __str__(self):
        return self.name
    
# Create Discussion Model
class Discussion(BaseModel):
    parent_id = models.IntegerField(blank=True, null=True)
    type = models.SmallIntegerField()
    content = models.TextField(blank=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='discussions')
    class Meta:
        ordering = ['-created_date'] # '-'->DESC
        
class Notification(BaseModel):
    isReaded = models.BooleanField(default=False)
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE, related_name='notification')

class AuctionHistory(BaseModel):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='author')
    user_id = models.IntegerField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='auction_histories')
    price = models.BigIntegerField()
    status = models.CharField(max_length=20, default=STATUS_PENDING)

class Report(BaseModel):
    report_text = models.TextField()
    reporter = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    reported_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    report_type = models.CharField(max_length=20, default=NOT_STANDARD)
   