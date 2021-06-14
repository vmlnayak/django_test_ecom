from django.db import models
from django.utils.translation import pgettext_lazy
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Category(MPTTModel):
    title = models.CharField(max_length=50)
    parent = TreeForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, related_name='children',
                            verbose_name=pgettext_lazy('Category field', 'parent'))

    def __str__(self):
        return self.title

    class MPTTMeta:
        order_insertion_by = ['title']


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    category = models.ManyToManyField(Category, related_name='products')
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return '{} '.format(self.name)
