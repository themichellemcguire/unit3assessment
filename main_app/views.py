from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Item

# Define the home view
def home(request):
  return render(request, 'home.html')

class ItemCreate(CreateView):
    model = Item
    fields = '__all__'