from django.contrib import admin

# Register your models here.
from .models import Genre, Books, BookInstance, Author, Languages

admin.site.register(Genre)
#admin.site.register(Books)
#admin.site.register(BookInstance)
#admin.site.register(Author, AuthorAdmin)
admin.site.register(Languages)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre', 'language')

@admin.register(BookInstance)
class BookInstance(admin.ModelAdmin):
    list_display = ()