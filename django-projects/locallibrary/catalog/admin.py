from django.contrib import admin

# Register your models here.
from .models import Genre, Books, BookInstance, Author, Languages

admin.site.register(Genre)
#admin.site.register(Books)
#admin.site.register(BookInstance)
#admin.site.register(Author, AuthorAdmin)
admin.site.register(Languages)

class BooksInline(admin.TabularInline):
    model = Books
    readonly_fields = ('title', 'isbn', 'genre', 'language')
    can_delete = False
    extra = 0

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline]

class BookInstanceInline(admin.TabularInline):
    model = BookInstance
    readonly_fields = ('id', 'status', 'due_back')
    can_delete = False
    extra = 0

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre', 'language')
    list_filter = ('language', 'author')
    fieldsets = (
        ('Basic Info',{
            'fields': ('title', 'author', 'language')
        }),
        ('Other Info', {
            'fields': ('summary', 'isbn', 'genre')
        }),
    )
    inlines = [BookInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'id', 'imprint', 'status', 'due_back')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )