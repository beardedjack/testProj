from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from testSite.models import Category, Good
from django.core.paginator import Paginator, InvalidPage

def index(request, id):
    try:
        page_num = request.GET["page"]
    except KeyError:
        page_num = 1
    cats = Category.objects.all().order_by("name")
    if id == None:
        cat = Category.objects.first()
    else:
        cat = Category.objects.get(pk = id)
    paginator = Paginator(Good.objects.filter(category=cat).order_by("name"), 3)
    try:
        goods = paginator.page(page_num)
    except InvalidPage:
        goods = paginator.page(1)
    allgoods = Good.objects.filter(category=cat).order_by("name")
    pricesum = 0
    for good in allgoods:
        pricesum = pricesum + good.price
    goodscount = allgoods.count
    return render(request, "index.html", {"category": cat, "cats": cats, "goods": goods, "goodscount":goodscount, "pricesum": pricesum})

def good(request, id):
    try:
        page_num = request.GET["page"]
    except KeyError:
        page_num = 1




    cats = Category.objects.all().order_by("name")
    try:
        good = Good.objects.get(pk = id)
    except Good.DoesNotExist:
        return HttpResponse("<b>Нет такого товара (" + str(id) + ")</b>" + "<br>")
    return render(request, "good.html", {"cats":cats, "good":good, "pn":page_num})