from django.contrib import admin

# Register your models here.
from .models import Genre, Books, BookInstance, Author, Languages

admin.site.register(Genre)
admin.site.register(Books)
admin.site.register(BookInstance)
admin.site.register(Author)
admin.site.register(Languages)