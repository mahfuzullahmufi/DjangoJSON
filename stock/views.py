import json
from multiprocessing import context
from pathlib import Path
from django.shortcuts import render, redirect
import json, os
import stock

from stock.models import Stock
from .forms import EditForm

# Create your views here.
def index(request):
    data = Stock.objects.all()

    return render(request, "stock/index.html", {"data": data})

def createData(request):
    form = EditForm()

    if request.method == 'POST':
        form = EditForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'stock\create.html', context)

def editData(request, pk):
    data = Stock.objects.get(id=pk)
    form = EditForm(instance=data)

    if request.method == 'POST':
        form = EditForm(instance=data, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'stock\edit_form.html', context)

def deleteData(request, pk):
    data = Stock.objects.get(id=pk)

    if request.method == "POST":
        data.delete()
        return redirect('/')

    context={'item': data}
    return render(request, 'stock\delete.html', context)

