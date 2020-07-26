from django.contrib import admin
from blog.models import Post

# Register your models here.
# admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('javascript/tinyMce.js')