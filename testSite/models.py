from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(verbose_name="Наименование", max_length = 30, unique = True)
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Good(models.Model):
    name = models.CharField(verbose_name="Наименование", max_length = 50, unique = True)
    description = models.TextField(verbose_name="Описание")
    in_stock = models.BooleanField(verbose_name="В наличии", default = True, db_index = True)
    category = models.ForeignKey(Category)
    price = models.DecimalField(verbose_name="Стоимость", decimal_places = 2, max_digits = 8, default = 0)

    def get_is_stock(self):
        if self.in_stock:
            return "+"
        else:
            return ""

    def __str__(self):
        s = self.name + " (" + Category.objects.get(pk = self.category.pk).name + ")"

        if not self.in_stock:
            s = s + " (нет в наличии) "

        if not self.price > 0:
            s = s + " (нет стоимости)"

        return s

    class Meta:
        ordering = ["-price", "name"]
        unique_together = ("category", "name", "price")
        verbose_name = "товар"
        verbose_name_plural = "товары"