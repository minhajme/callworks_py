from django.shortcuts import render


def dashboard(request):
    data = {}
    return render(request, 'sbadmin2/index.html', data)
