from django.db import models
from django.shortcuts import resolve_url


class Category(models.Model):
    #속성
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, allow_unicode=True, unique=True)
    #class Meta
    class meta:
        ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    #__str__()
    def __str__(self):
        return self.name
    #get_absolute_url()
    def get_absolute_url(self):
        return resolve_url('shop:category_detail', self.slug)

class Product(models.Model):
    name = models.CharField(max_length=100)
    sluge = models.SlugField(max_length=100, allow_unicode=True, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    image = models.ImageField(upload_to='products/%Y/%m/%d', default='products/mo_image.jpg')
    stock = models.PositiveIntegerField()
    description = models.TextField(blank=True)

    available_display = models.BooleanField('Display', default=True)
    available_order = models.BooleanField('Order', default=True)

    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return resolve_url('shop:product_detail', self.id, self.slug)
    #name
    #price
    #category
    #image
    #stock
    #description

    #class Meta
    #__str__()
    #get_absolute_url()
