from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone
from datetime import timedelta
from blog.task import PublicPosts
from blog.models import Post


class GetAlreadyPublPostTest(TestCase):
    """Класс для тестирования получения готовых постов для публикации"""

    def setUp(self):
        """Метод класса для изменяемых объектов"""
        
        self.posts = Post

        self.user = User.objects.create_superuser(
            username='test_admin',
            password='test_psswd'
        )

        for counter, _ in enumerate(range(0, 2), start=1):
            self.posts.objects.create(
                author=self.user,
                title=f'test{counter}',
                text=f'test{counter} text',
                created_at=timezone.now()-timedelta(minutes=1)
            )
        
        self.get_posts_ready_pub = PublicPosts().get_ready_post_bubl(self.posts)

    def test_get_post_publ_true(self):
        """Метод класса проверит есть ли внутри данные"""
        
        self.assertTrue(self.get_posts_ready_pub)

    def test_get_post_publ_equel_class(self):
        """Метод класса проверит что внутри класс QuerySet"""
        
        self.assertEqual(
            str(type(self.get_posts_ready_pub)), 
            "<class 'django.db.models.query.QuerySet'>"
        )

    def test_get_post_publ_equel_title(self):
        """Метод класса проверит title на содержимое"""

        get_title = self.get_posts_ready_pub.get(id=1).title
        self.assertEqual(get_title, 'test1')

    def test_get_post_publ_equel_author(self):
        """Метод класса проверит author на содержимое"""

        get_author = self.get_posts_ready_pub.get(id=1).author
        self.assertEqual(get_author, self.user)
    
    def test_get_post_publ_equel_text(self):
        """Метод класса проверит text на содержимое"""

        get_text = self.get_posts_ready_pub.get(id=2).text
        self.assertEqual(get_text, 'test2 text')
