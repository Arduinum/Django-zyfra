from django.db import models
from django.conf import settings
from django.utils import timezone


class Post(models.Model):
    """Класс описывает модель публикации записи блога"""

    author = models.ForeignKey(
        verbose_name='автор',
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    title = models.CharField(
        verbose_name='название',
        max_length=200
    )

    text = models.TextField(
        verbose_name='содержимое'
    )

    created_at = models.DateTimeField(
        verbose_name='создан',
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        verbose_name='обновлён',
        auto_now=True
    )

    published_at = models.DateTimeField(
        verbose_name='опубликован',
        blank=True,
        null = True
    )

    def publish(self):
        """Метод класса для вставки даты публикации"""
        self.published_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title
