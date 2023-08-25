from django.http import HttpResponse
from django.template import loader
from .models import Member

def books(request):
  mybooks = Book.objects.all().values()
  template = loader.get_template('all_books.html')
  context = {
    'mybooks': mybooks,
  }
  return HttpResponse(template.render(context, request))