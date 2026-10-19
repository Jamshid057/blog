# Mening blogim

O‘zbekcha shaxsiy blog. Django 5.2, SQLite, mobilga mos HTML/CSS. Post yozish va tahrirlash Django admin orqali. Qidiruv, mavzu bo‘yicha saralash, sahifalash va o‘qish vaqti mavjud.

## Ishga tushirish

Python 3.10 yoki yangirog‘i kerak:

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Sayt: http://127.0.0.1:8000/
Admin: http://127.0.0.1:8000/admin/

Admin panelda avval mavzu, keyin maqola qo‘shing. «Chop etilgan» belgisini yoqing. Kelajak vaqti qo‘yilgan maqolalar belgilangan vaqtdan boshlab ko‘rinadi. `slug` avtomatik to‘ldiriladi; zarur bo‘lsa lotin harflari bilan tahrirlang. Maqola matni oddiy matn: bo‘sh qator yangi paragraf yaratadi. HTML xavfsizlik uchun matn sifatida chiqariladi.

«Men haqimda» matni va blog nomini `templates/base.html` va `templates/posts/list.html` fayllarida o‘zgartiring. Dizayn `static/css/style.css` faylida.

## Tekshiruv

```sh
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py test
```

## Hosting

Hozircha lokal loyiha; internetga joylanmagan. Ishlab chiqarish muhiti uchun `DJANGO_SECRET_KEY`, `DJANGO_DEBUG=0`, `DJANGO_ALLOWED_HOSTS` qiymatlarini belgilang, WSGI server va static fayllar xizmatini sozlang. SQLite bazasini muntazam zaxiralang. `runserver` ishlab chiqarish serveri emas.
