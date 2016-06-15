from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 30, unique = True)
    description = models.TextField()

    def __str__(self):
        return self.name



class Good(models.Model):
    name = models.CharField(max_length = 5, unique = True)
    description = models.TextField()
    in_stock = models.BooleanField(default = True, db_index = True)
    category = models.ForeignKey(Category)
    price = models.DecimalField(decimal_places = 2, max_digits = 8, default = 0)

    def get_is_stock(self):
        if self.in_stock:
            return "+"
        else:
            return ""

    def __str__(self):
        s = self.name
        if not self.in_stock:
            s = s + " (нет в наличии)"
        return s

    class Meta:
        ordering = ["-price", "name"]
        unique_together = ("category", "name", "price")
        verbose_name = "товар"
        verbose_name_plural = "товары"