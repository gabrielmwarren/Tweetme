from django.contrib import admin
from blog.models import Post, Comment, Preference

admin.site.site_header = 'Tweetme Dashboard'


class PostAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Preference)
