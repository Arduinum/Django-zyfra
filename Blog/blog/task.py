from django.utils import timezone
from datetime import timedelta
from celery import shared_task
import logging
from blog.models import Post


logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s %(message)s]')
logger = logging.getLogger(__name__)


class PublicPosts:
    """Класс для работы с публикациями постов"""

    @staticmethod    
    def get_ready_post_bubl(model_post):
        """Метод класса для фильтрации постов, готовых к публикации"""
        return model_post.objects.filter(
            is_published=False, 
            created_at__lte=timezone.now()-timedelta(minutes=1)
        )
    
    @staticmethod
    def set_post_publ(queryset_posts):
        """Метод класса для публикации постов"""

        try:
            for post in queryset_posts:
                post.is_published = True
                post.published_at = timezone.now()
                post.save()
        except Exception as err:
            logger.error(f'Ошибка сохранения данных поста - {err}!')


@shared_task()
def publishing_posts():
    post = Post
    publ_posts = PublicPosts()
    filter_posts = publ_posts.get_ready_post_bubl(post)
    publ_posts.set_post_publ(filter_posts)
    if filter_posts:
        logger.info(f'{filter_posts}')
        logger.info('Новые посты успешно опубликованы!')
