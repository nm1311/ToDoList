from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone
from .models import Todolist
from .forms import AddItemForm
from django.views.decorators.http import require_POST

def index(request):
    items =  Todolist.objects.all().order_by('add_time')
    form = AddItemForm()
    return render(request, 'App_toDoList/index.html',{'form':form, 'items':items})

@require_POST
def add_item(request):
    form = AddItemForm(request.POST)

    if form.is_valid:
        new_item = Todolist(item_name=request.POST['item_name'], is_complete=False, is_important=False, add_time=timezone.now())
        new_item.save()

    return redirect('index')

def item_complete(request, pk):
    item = get_object_or_404(Todolist,pk=pk)
    item.is_complete=True
    item.save()

    return redirect('index')

def delete_item(request,pk):
    Todolist.objects.get(pk=pk).delete()
    return redirect('index')

def delete_item_from_impt(request,pk):
    Todolist.objects.get(pk=pk).delete()
    return redirect('show_impt')


def delete_completed(request):
    Todolist.objects.filter(is_complete=True).delete()
    return redirect('index')


def reset(request):
    Todolist.objects.all().delete()
    return redirect('index')


def mark_impt(request,pk):
    item = get_object_or_404(Todolist,pk=pk)
    item.is_important=True
    item.save()
    return redirect('index')

def show_impt(request):
    items = Todolist.objects.filter(is_important=True)
    return render(request,'App_toDoList/show_impt.html', {'items':items})

def remove_impt(request, pk):
    item = get_object_or_404(Todolist,pk=pk)
    item.is_important = False
    item.save()

    return redirect('index')