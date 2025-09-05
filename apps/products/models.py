from django.db import models
from apps.pages.models import BaseModel


class CatalogModel(BaseModel):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Catalog'
        verbose_name_plural = 'Catalogs'


class CategoryModel(BaseModel):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class ColorModel(BaseModel):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Color'
        verbose_name_plural = 'Colors'


class TagModel(BaseModel):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class ProductModel(BaseModel):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    catalog = models.ForeignKey(CatalogModel, on_delete=models.CASCADE)
    description = models.TextField(blank=True)

    colors = models.ManyToManyField(ColorModel, blank=True)
    tags = models.ManyToManyField(TagModel, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'