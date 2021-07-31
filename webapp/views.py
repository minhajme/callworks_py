from django.shortcuts import render
from django.shortcuts import redirect


def index(request):
    return redirect('dashboard')


def dashboard(request):
    data = {}
    return render(request, 'sbadmin2/index.html', data)
