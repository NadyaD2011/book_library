from django.contrib import admin  
from .models import Movie, Genre
from django.shortcuts import reverse
from django.utils.html import format_html
from django.templatetags.static import static


class MovisAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'rating')
    list_filter = ('release_year', 'genre', 'rating')
    search_fields = [
        'title',
        'director',
        'genre'
    ]
    readonly_fields = [
        'get_image_preview',
    ]

    def get_image_preview(self, obj):
        if not obj.poster:
            return 'выберите картинку'
        return format_html('<img src="{url}" style="max-height: 200px;"/>', url=obj.poster.url)

    get_image_preview.short_description = 'превью'


class GenreAdmin(admin.ModelAdmin):
    search_fields = [
        'name',
    ]


admin.site.register(Movie, MovisAdmin)
admin.site.register(Genre, GenreAdmin)
