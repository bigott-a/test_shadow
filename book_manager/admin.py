from django.contrib import admin

from book_manager.models import Author, Book

models = (
    Author,
    Book,
)

for model in models:
    admin.site.register(model)
