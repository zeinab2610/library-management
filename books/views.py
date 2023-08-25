from django.http import HttpResponse
from django.template import loader
from .models import Book

def books(request):
  mybooks = Book.objects.all().values()
  template = loader.get_template('all_books.html')
  context = {
    'mybooks': mybooks,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
    mybook = Book.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mybook': mybook,
    }
    return HttpResponse(template.render(context, request))
    
def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())