from django.views.generic.base import TemplateView
from django.core.paginator import Paginator, InvalidPage
from testSite.models import Category, Good
from django.http import Http404

class GoodListView(TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super(GoodListView, self).get_context_data(**kwargs)

        try:
            page_num = self.request.GET["page"]
        except KeyError:
            page_num = 1
        context["cats"] = Category.objects.order_by("name")

        iid = kwargs["id"]

        if kwargs["id"] == None:
            context["category"] = Category.objects.first()
        else:
            context["category"] = Category.objects.get(pk = kwargs["id"])
        paginator = Paginator(Good.objects.filter(category=context["category"]).order_by("name"), 3)
        try:
            context["goods"] = paginator.page(page_num)
        except InvalidPage:
            context["goods"] = paginator.page(1)

        allgoods = Good.objects.filter(category=iid).order_by("name")
        context["goodscount"] = allgoods.count
        pricesum = 0
        for good in allgoods:
            pricesum = pricesum + good.price
        context["pricesum"] = pricesum
        return context

class GoodDetailView(TemplateView):
    template_name = "good.html"
    def get_context_data(self, **kwargs):
        context = super(GoodDetailView, self).get_context_data(**kwargs)
        try:
            context["pn"] = self.request.GET["page"]
        except KeyError:
            context["pn"] = 1
        context["cats"] = Category.objects.order_by("name")
        try:
            context["good"] = Good.objects.get(pk = kwargs["id"])
        except Good.DoesNotExist:
            raise Http404("Нет такого товара")

        return context


