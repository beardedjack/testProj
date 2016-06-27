from django.views.generic.base import TemplateView
from django.core.paginator import Paginator, InvalidPage
from testSite.models import Category, Good
from django.http import Http404

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.views.generic.base import ContextMixin


class GoodListView(ListView):
    template_name = "index.html"
    paginate_by = 10
    cat = None

    def get(self, request, *args, **kwargs):
        if self.kwargs["id"] == None:
            self.cat = Category.objects.first()
        else:
            self.cat = Category.objects.get(pk = self.kwargs["id"])
        return super(GoodListView, self).get(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super(GoodListView, self).get_context_data(**kwargs)
        context["cats"] = Category.objects.order_by("name")
        context["category"] = self.cat
        return context

    def get_queryset(self):
        return Good.objects.filter(category=self.cat).order_by("name")




        # allgoods = Good.objects.filter(category=iid).order_by("name")
        # context["goodscount"] = allgoods.count
        # pricesum = 0
        # for good in allgoods:
        #     pricesum = pricesum + good.price
        # context["pricesum"] = pricesum
        # return context


class GoodDetailView(DetailView):
    template_name = "good.html"
    model = Good
    pk_url_kwarg = "id"

    def get_context_data(self, **kwargs):
        context = super(GoodDetailView, self).get_context_data(**kwargs)
        try:
            context["pn"] = self.request.GET["page"]
        except KeyError:
            context["pn"] = "1"
        context["cats"] = Category.objects.order_by("name")
        return context

    #
    # def get_context_data(self, **kwargs):
    #     context = super(GoodDetailView, self).get_context_data(**kwargs)
    #     try:
    #         context["pn"] = self.request.GET["page"]
    #     except KeyError:
    #         context["pn"] = 1
    #     context["cats"] = Category.objects.order_by("name")
    #     try:
    #         context["good"] = Good.objects.get(pk = kwargs["id"])
    #     except Good.DoesNotExist:
    #         raise Http404("Нет такого товара")
    #
    #     return context


