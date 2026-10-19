# Database
SQLite at ignored `db.sqlite3`. Category: unique name and slug. Post: title, unique slug, excerpt, plain-text body, published flag, publication time, update time, optional category. Deleting a category retains posts with null category. Initial migration in posts/migrations/0001_initial.py. Django auth stores admin users; no default credentials.
