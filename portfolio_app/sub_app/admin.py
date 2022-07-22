from django.contrib import admin
from .models import Category, Post,PaperCat,Papers
# Register your models here.

# for configuration of Category admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'add_date')
    search_fields = ('title',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title','add_date')
    search_fields = ('title',)
    list_filter = ('category',)
    list_per_page = 10

class PapersAdmin(admin.ModelAdmin):
    list_display = ('title','category','date')
    search_fields = ('title','category')
    list_filter = ('category','date')
    list_per_page = 10


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(PaperCat)
admin.site.register(Papers, PapersAdmin)