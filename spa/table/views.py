from django.shortcuts import render
from .forms import FilterForm
from .models import Table


def index(request):
    tables = Table.objects.all()
    form = FilterForm()
    return render(request, 'index.html', {'tables': tables, 'form': form})


def filter(request):
    if request.method == 'POST':
        form = FilterForm(request.POST)
        colum = form.data['colum']
        condition = form.data['condition']
        text = form.data['text']
        if colum == 'name':
            if condition == '=':
                tables = Table.objects.filter(name=text)
            elif condition == 'more':
                tables = Table.objects.filter(name__gt=text)
            elif condition == 'less':
                tables = Table.objects.filter(name__lt=text)
            tables = Table.objects.filter(name__contains=text)
            return render(
                request, 'index.html', {'tables': tables, 'form': form})
        elif colum == 'count':
            if condition == '=':
                tables = Table.objects.filter(count=text)
            elif condition == 'more':
                tables = Table.objects.filter(count__gt=text)
            elif condition == 'less':
                tables = Table.objects.filter(count__lt=text)
            else:
                tables = Table.objects.filter(count__contains=text)
            return render(
                request, 'index.html', {'tables': tables, 'form': form})
        else:
            text = int(text)
            if condition == '=':
                tables = Table.objects.filter(distance=text)
            elif condition == 'less':
                tables = Table.objects.filter(distance__lt=text)
            elif condition == 'more':
                tables = Table.objects.filter(distance__gt=text)
            else:
                tables = Table.objects.filter(distance__contains=text)
            return render(
                request, 'index.html', {'tables': tables, 'form': form})
