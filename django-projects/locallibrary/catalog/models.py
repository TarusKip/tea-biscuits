from django.db import models
from django.urls import reverse 
import uuid
# Used to generate URLs by reversing the URL patterns

# Create your models here.

class Genre(models.Model):
    # Model representing the book genre
    name = models.CharField(max_length=200, help_text='Enter the book genre, e.g., Sci-Fi')

    def __str__(self):
        # String for representng the Model object
        return self.name
    

class Books(models.Model):
    # Model representing a book in general, not a praticular physical copy of the book
    title = models.CharField(max_length=200)

    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    # Foreign key because a book can only have one author, but author can have multiple books
    # Author is a string rather than an object because it has not yet been declared in the file

    summary = models.CharField(max_length=1000, help_text='Enter a brief description of the book')

    isbn = models.CharField('ISBN', max_length=13, unique=True, help_text=
        '13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')
    # A genre can contain may books, books can cover many genres
    # Genre class has already been defined so we can specify the object above

    def display_genre(self):
        return ', '.join(genre.name for genre in self.genre.all()[:3])
    display_genre.short_description = 'Genre'

    language = models.ForeignKey('Languages', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        # string for representing the model object
        return self.title
    
    def get_absolute_url(self):
        # returns a URL to access a detail record for this book
        return reverse('book-detail', args=[str(self.id)])
    
class BookInstance(models.Model):
    # Model representing a specific copy of a book
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, 
                          help_text='Unique ID for this particular book across the whole library')
    
    book = models.ForeignKey('Books', on_delete=models.RESTRICT, null=True)

    imprint = models.CharField(max_length=200)

    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability',
    )


class Meta:
    ordering = ['due_back']

    def __str__(self):
        # String for representing the model object
        return f'{self.id ({self.book.title})}'
    

class Author(models.Model):
    #Model representing the Author
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['first_name', 'last_name']
        
    def get_absolute_url(self):
        # returns a URL to access a particular Author instance
        return reverse('author-detail', args=[str(self.id)])
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    

class Languages(models.Model):
    #Model representing the language a book is written in
    name = models.CharField(max_length=100, help_text='Enter the books language e.g., English, Kiswahili')

    def __str__(self):
        return self.name
