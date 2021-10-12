from django.test import TestCase
from django.urls import reverse
from .models import Post, Category
from django.contrib.auth.models import User

class BlogModelTest(TestCase):

  def post_create(self):
    author = User.objects.create(username="eslam", password="1q2w3e4r5t6y") 
    category = Category.objects.create(name="test category")

    return Post.objects.create(
          author=author,
          title="django testing",
          tags="django",
          description="django testing description",
          category = category,

    )

  def test_model_str(self):
    post = self.post_create()
    self.assertEqual(post.__str__(), post.title)

  
class BlogViewTest(TestCase):

  def test_blog_url(self):
    response = self.client.get("/blog")
    self.assertEqual(response.status_code, 200)

  def test_view_reverse(self):
    response = self.client.get(reverse('blog:post_list'))
    self.assertTemplateUsed(response, 'blog/post_list.html')


   