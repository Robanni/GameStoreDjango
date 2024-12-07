from django.db import models

class Game(models.Model):
    title = models.CharField(
        max_length=100, 
        unique=True, 
        null=False, 
        verbose_name="Название"  # Для отображения в админке
    )
    description = models.TextField(
        max_length=500, 
        null=False, 
        verbose_name="Описание"
    )
    main_image_url = models.URLField(
        max_length=200, 
        verbose_name="Ссылка на главную картинку"
    )
    footage_images = models.JSONField(
        verbose_name="Ссылки на картинки игры"
    )
    genres = models.JSONField(
        verbose_name="Жанры", 
        help_text="Список жанров игры"
    )
    os = models.CharField(
        max_length=100, 
        verbose_name="Операционная система", 
        help_text="Например: Windows, macOS, Linux"
    )
    publisher = models.CharField(
        max_length=100, 
        verbose_name="Издатель"
    )
    developer = models.CharField(
        max_length=100, 
        verbose_name="Разработчик"
    )
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Добавлено")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Игра"
        verbose_name_plural = "Игры"
        ordering = ['title']  # Упорядочивание по названию
