from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(verbose_name='имя', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)
    is_active = models.BooleanField(db_index=True, verbose_name='активна', default=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='имя продукта', max_length=128)
    image = models.ImageField(upload_to='products_images', blank=True)
    short_desc = models.CharField(verbose_name='краткое описание продукта', max_length=60, blank=True)
    description = models.TextField(verbose_name='описание продукта', blank=True)
    price = models.DecimalField(verbose_name='цена продукта', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='количество на складе', default=0)
    is_active = models.BooleanField(db_index=True, verbose_name='активна', default=True)

    def __str__(self):
        return "{} ({})".format(self.name,self.category.name)

    @staticmethod
    def get_items():
        return Product.objects.filter(is_active=True).order_by('category', 'name')


class VisualModels(models.Model):
    name = models.CharField(verbose_name='слоган', max_length=128)
    description = models.TextField(verbose_name='подробное описание', blank=True)
    image = models.ImageField(upload_to='visual_images', blank=True)

    def __str__(self):
        return self.name

