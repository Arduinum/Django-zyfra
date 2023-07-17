from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
from PIL import Image
from sys import getsizeof


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

    photo = models.ImageField(
        verbose_name='фото',
        upload_to='blog',
        blank=True
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

    def save_img(self):
        """Метод для сохранения ужатого изображения"""
        if not self.id:
            self.photo = self.compress_img(self.photo)

    def compress_img(self, img):
        """Метод класса для сжатия изображения"""
        try:
            # открываем исходное img
            img_transitory = Image.open(img)
            # объект для работы с байтами файла
            work_bytes = BytesIO()
            # изменение размера img
            # img_resized = img_transitory.resize((800, 600))
            name_jpg = f'{img.name.split(".")[0]}.jpg'
            # сохраняем изменённое изображение с качеством 60
            img_transitory.save(fp=work_bytes, format='JPEG', quality=60)
            work_bytes.seek(0)  # установка позиции чтения/записи в начало объекта
            # создаём оптимизированную версию изображения
            img = InMemoryUploadedFile(
                file=work_bytes, 
                field_name='imageField', 
                name=name_jpg,
                content_type='image/jpeg',
                size=getsizeof(work_bytes),
                charset=None
            )
            return img
        except Exception as err:
            print(err)
        return img

    def __str__(self):
        return self.title
