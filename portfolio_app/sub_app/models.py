from django.db import models
from ckeditor.fields import RichTextField

##add image alt tag and description excerpt

class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=60)
    # description = models.TextField()
    slug = models.CharField(max_length=30)
    image = models.ImageField(upload_to='category/')
    add_date = models.DateTimeField(auto_now_add=True, null=False)
    summary=models.CharField(max_length=150,null=True)
    class Meta: verbose_name_plural = 'BlogCategories'
    def __str__(self):
        return self.title

# Post Mode
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=60)
    content = RichTextField()
    slug = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post/')
    add_date = models.DateTimeField(auto_now_add=True, null=False)
    summary=models.CharField(max_length=150,null=True,blank=True)
    class Meta: verbose_name_plural = 'BlogPosts'
    def __str__(self):
        return self.title


# paper categories such as conference, journal, workshops
class PaperCat(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=60)
    class Meta: verbose_name_plural = 'PaperCategories'
    def __str__(self):
        return self.title

class Papers(models.Model):
    paper_id=models.AutoField(primary_key=True)
    title= models.CharField(max_length=200)
    abstract=RichTextField()
    date=models.DateField(null=True,blank=True)
    publisher=models.CharField(max_length=200)
    paper_url=models.CharField(max_length=100)
    github_url=models.CharField(max_length=100,null=True,blank=True)
    category = models.ForeignKey(PaperCat, on_delete=models.CASCADE)
    class Meta: verbose_name_plural = 'PapersPublished'
    def __str__(self):
        return self.title
    
    