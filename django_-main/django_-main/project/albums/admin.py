from django.contrib import admin
from .models import Musician, Albums, Tag, Category, Article

@admin.register(Musician)
class MusicianAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name')
    list_display = ('first_name', 'last_name', 'instrument')


@admin.register(Albums)
class AlbumsAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_filter = ('name', )
    list_display = ('artist', 'name', 'date', 'stars')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name',)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title', 'category')
    list_filter = ('category', 'tags')
