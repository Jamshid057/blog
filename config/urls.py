from django.contrib import admin
from django.urls import path
from posts import views
urlpatterns = [path("admin/", admin.site.urls), path("", views.post_list, name="post_list"), path("maqola/<slug:slug>/", views.post_detail, name="post_detail")]
admin.site.site_header = "Mening blogim"
admin.site.site_title = "Blog boshqaruvi"
admin.site.index_title = "Maqolalarni boshqarish"
