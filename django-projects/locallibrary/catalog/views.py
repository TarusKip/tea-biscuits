from django.shortcuts import render
from django.db.models.functions import Lower

# Create your views here.
from .models import Books, Author, BookInstance, Genre

def index(request):
    '''View function for the home page'''
    
    # Generating counts
    num_books = Books.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_genres = Genre.objects.all().count()

    # Available books
    num_instances_available = BookInstance.objects.filter(status='a').count()

    # The "All()" is implied by default
    num_authors = Author.objects.count()

    # Titles with the word flower in it
    num_flower = Books.objects.annotate(lower_title=Lower('title')).filter(lower_title__contains='flower').count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
        'num_flower': num_flower
    }

    # Render the template index.html with the data in the context var
    return render(request, 'index.html', context=context)