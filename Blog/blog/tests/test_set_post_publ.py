from django.contrib.auth.models import User
from django.test import TestCase
from blog.task import PublicPosts
from blog.models import Post


class SetAlreadyPublPostTest(TestCase):
    """Класс для тестирования публикации готовых постов для публикации"""

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
                text=f'test{counter} text'
            )
        
        PublicPosts().set_post_publ(self.posts.objects.all())
    
    def test_set_post_publ_true_1(self):
        """Тест проверит первый пост на статус is_published"""

        self.assertTrue(self.posts.objects.get(id=1).is_published, True)
    
    def test_set_post_publ_true_2(self):
        """Тест проверит второй пост на статус is_published"""

        self.assertTrue(self.posts.objects.get(id=2).is_published, True)

    def test_set_post_publ_is_datetime(self):
        """Тест проверит является ли класс данных datetime.datetime"""

        self.assertEqual(
            str(type(self.posts.objects.get(id=1).published_at)), 
            "<class 'datetime.datetime'>"
        )
