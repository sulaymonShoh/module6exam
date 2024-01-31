from django.contrib import admin
from sulaymonqori.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "author"]
    search_fields = ["title", ]
    list_filter = ["author", ]
