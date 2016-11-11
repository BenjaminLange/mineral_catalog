from django.shortcuts import render, redirect
import random

from .models import Mineral


def index(request):
    minerals = Mineral.objects.all()
    return render(request, 'minerals/index.html', {'minerals': minerals})


def detail(request, pk):
    mineral = Mineral.objects.get(pk=pk)
    return render(request, 'minerals/detail.html', {'mineral': mineral})


def random(request):
    mineral = Mineral.objects.all().order_by('?')[0]
    return redirect('minerals:detail', pk=mineral.pk)
    # return render(request, 'minerals/detail.html', {'mineral': mineral})
