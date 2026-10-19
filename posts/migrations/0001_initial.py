from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(name="Category", fields=[("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")), ("name", models.CharField(max_length=80, unique=True, verbose_name="Nomi")), ("slug", models.SlugField(unique=True, verbose_name="Havola nomi"))], options={"verbose_name": "Mavzu", "verbose_name_plural": "Mavzular", "ordering": ["name"]}),
        migrations.CreateModel(name="Post", fields=[("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")), ("title", models.CharField(max_length=200, verbose_name="Sarlavha")), ("slug", models.SlugField(max_length=220, unique=True, verbose_name="Havola nomi")), ("excerpt", models.CharField(max_length=350, verbose_name="Qisqa tavsif")), ("body", models.TextField(verbose_name="Maqola matni")), ("is_published", models.BooleanField(default=False, verbose_name="Chop etilgan")), ("published_at", models.DateTimeField(default=django.utils.timezone.now, verbose_name="Chop etish vaqti")), ("updated_at", models.DateTimeField(auto_now=True)), ("category", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="posts", to="posts.category", verbose_name="Mavzu"))], options={"ordering": ["-published_at", "-pk"], "verbose_name": "Maqola", "verbose_name_plural": "Maqolalar"}),
    ]
