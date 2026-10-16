from django.contrib import admin

# Register your models here.

from django.contrib import admin
from blog.models import Comment, Category, Post

#Aqui se configura o que aparece para o admin de cada tabela
class CategoryAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)


