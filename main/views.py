from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
# Create your views here.
def urlviews(request,korzina):
    if korzina==None:
        return render(request, "main.html")
    elif korzina=="page1":
        return render(request, "main.html")
    elif korzina=="page2":
        return render(request, "main.html")
    else:
        return HttpResponseNotFound("<h1>Страница не найдена</h1>")