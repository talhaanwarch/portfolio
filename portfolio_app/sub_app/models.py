from django.db import models
from ckeditor.fields import RichTextField

##add image alt tag and description excerpt

class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category/')
    add_date = models.DateTimeField(auto_now_add=True, null=False)
    summary=models.CharField(max_length=150,null=True)
    def __str__(self):
        return self.title

# Post Mode
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = RichTextField()
    slug = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post/')
    add_date = models.DateTimeField(auto_now_add=True, null=False)
    summary=models.CharField(max_length=150,null=True)
    def __str__(self):
        return self.title