# Architecture
`config/` owns settings, URL routing and WSGI. `posts/` owns models, admin and public views. `templates/` and `static/css/style.css` own presentation. All public post lookup passes through `published_posts()` which excludes drafts and future publication dates. Bodies use autoescaped plain text and paragraph formatting.
