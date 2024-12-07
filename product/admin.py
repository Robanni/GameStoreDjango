from django.contrib import admin

from .models import Game

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'publisher', 'developer','created_at')  # Поля для отображения в списке
    search_fields = ('title', 'publisher', 'developer')  # Поиск по этим полям
    list_filter = ('os', 'genres')  # Фильтры по операционной системе и жанрам