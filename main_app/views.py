from django.shortcuts import render, redirect
from .models import Item
from main_app.forms import Form
from django.views.generic.edit import CreateView
# Create your views here.
def home(request):
    item = Item.objects.all()
    form = Form()
    if request.POST:
        desc = request.POST.get('description', None)
        new_item = Item.objects.create(description=desc,)
        return render (request,'home.html', {'item': item, 'form': form})
    else:
        return render (request,'home.html', {'item': item, 'form': form})
class ItemCreate(CreateView):
    model = Item
    fields = '__all__'

def delete_item(request, pk):
    item = Item.objects.get(id=pk)
    print(item)
    item.delete()
    return redirect ('home')
