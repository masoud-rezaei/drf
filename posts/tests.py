from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post
# Create your tests here.
 
class Blogtest(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1=User.objects.create_user(username='testuser1',password='Ramz1234')
        testuser1.save()

        test_post =Post.objects.create(author=testuser1,title='Blog title',body='body content ...')
        test_post.save()

    def test_blog_content(self):
        post=Post.objects.get(id=1)
        author=f'{post.author}'
        body=f'{post.body}'
        title=f'{post.title}'
        self.assertEqual(author,'testuser1')
        self.assertEqual(title,'Blog title')
        self.assertEqual(body,'body content ...')