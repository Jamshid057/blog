from django.db import models
from django.urls import reverse
from django.utils import timezone

class Category(models.Model):
    name = models.CharField("Nomi", max_length=80, unique=True)
    slug = models.SlugField("Havola nomi", unique=True)
    class Meta:
        verbose_name = "Mavzu"
        verbose_name_plural = "Mavzular"
        ordering = ["name"]
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField("Sarlavha", max_length=200)
    slug = models.SlugField("Havola nomi", unique=True, max_length=220)
    category = models.ForeignKey(Category, verbose_name="Mavzu", on_delete=models.SET_NULL, null=True, blank=True, related_name="posts")
    excerpt = models.CharField("Qisqa tavsif", max_length=350)
    body = models.TextField("Maqola matni")
    is_published = models.BooleanField("Chop etilgan", default=False)
    published_at = models.DateTimeField("Chop etish vaqti", default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ["-published_at", "-pk"]
        verbose_name = "Maqola"
        verbose_name_plural = "Maqolalar"
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("post_detail", args=[self.slug])
    @property
    def reading_minutes(self):
        return max(1, (len(self.body.split()) + 199) // 200)
