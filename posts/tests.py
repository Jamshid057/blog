from datetime import timedelta
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import Category, Post

class BlogTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Texnologiya", slug="texnologiya")
        self.public = Post.objects.create(title="Python bilan tanishuv", slug="python", excerpt="Birinchi qadam", body="Django haqida qaydlar", is_published=True, category=self.category)
        self.draft = Post.objects.create(title="Maxfiy qoralama", slug="qoralama", excerpt="Tayyor emas", body="Yashirin")
        self.future = Post.objects.create(title="Kelajak yozuvi", slug="kelajak", excerpt="Keyinroq", body="Reja", is_published=True, published_at=timezone.now() + timedelta(days=1))

    def test_public_listing_excludes_drafts_and_future_posts(self):
        response = self.client.get(reverse("post_list"))
        self.assertContains(response, self.public.title)
        self.assertNotContains(response, self.draft.title)
        self.assertNotContains(response, self.future.title)

    def test_hidden_posts_cannot_be_opened_directly(self):
        for post in [self.draft, self.future]:
            self.assertEqual(self.client.get(post.get_absolute_url()).status_code, 404)

    def test_search_and_category_filter(self):
        response = self.client.get(reverse("post_list"), {"q": "Django", "mavzu": self.category.slug})
        self.assertContains(response, self.public.title)
        self.assertNotContains(self.client.get(reverse("post_list"), {"q": "topilmaydi"}), self.public.title)

    def test_article_escapes_html(self):
        self.public.body = '<script>alert("x")</script>'
        self.public.save()
        response = self.client.get(self.public.get_absolute_url())
        self.assertContains(response, "&lt;script&gt;")
        self.assertNotContains(response, '<script>')

    def test_admin_requires_login(self):
        self.assertRedirects(self.client.get(reverse("admin:posts_post_add")), "/admin/login/?next=/admin/posts/post/add/")
