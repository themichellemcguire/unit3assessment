from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView
from .models import Item

# Define the home view
def home(request):
    items = Item.objects.all()
    count = items.count()
    return render(request, 'home.html', {'item_list': items, 'count': count})

class ItemCreate(CreateView):
    model = Item
    fields = '__all__'
    success_url = ''

class ItemDelete(DeleteView):
    model = Item
    success_url = '/'