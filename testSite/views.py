from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from testSite.models import Category, Good

def index(request, id):
    if id == None:
        cat = Category.objects.first()
    else:
        cat = Category.objects.get(pk = id)
    goods = Good.objects.filter(category = cat).order_by("name")
    s = "Категория: " + cat.name + "<br><br>"
    for good in goods:
        s = s + "(" + str(good.pk) + ") " + good.name + "<br>"
    return HttpResponse(s)

def good(request, id):
    if id == None:
        s = "Не выбран id товара"
    else:
        try:
            goo = Good.objects.get(pk = id)
            s = "Товар (" + str(goo.pk) + "): " + goo.name + "<br>"
        except Good.DoesNotExist:
            s = "<b>Нет такого товара (" + str(id) + ")</b>" + "<br>"
    return HttpResponse(s)
