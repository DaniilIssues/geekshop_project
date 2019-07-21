from django.shortcuts import render
from .models import ProductCategory, Product, VisualModels
from basketapp.models import Basket
from django.shortcuts import get_object_or_404
import random
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_hot_product():
    products = Product.objects.all()

    return random.sample(list(products), 1)[0]


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:3]

    return same_products


def main(request):
    title = 'Главная'
    site_visual = VisualModels.objects.all()[:3]

    categories = ProductCategory.objects.all()

    products = Product.objects.all()[:4]

    context = {'title': title,
               'products': products,
               'categories': categories,
               'site_visual': site_visual,
               }
    return render(request, 'mainapp/index.html', context)


def products(request, pk=None, page=1):
    title = 'Продукты'
    links_menu = ProductCategory.objects.filter(is_active=True)
    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

    if pk is not None:
        if pk == 0:
            category = {
                'pk': 0,
                'name': 'все',
            }
            products = Product.objects.all().order_by('price')
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk, category__is_active=True).order_by('price')

        paginator = Paginator(products, 3)
        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)

        context = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products_paginator,
        }
        return render(request, 'mainapp/product_list.html', context)

    context = {
        'title': title,
        'links_menu': links_menu,
        'hot_product': hot_product,
        'same_products': same_products,
    }

    return render(request, 'mainapp/products.html', context)


def contact(request):
    title = 'Контакты'

    categories = ProductCategory.objects.all()
    context = {
        'title': title,
        'category': categories,

    }
    return render(request, 'mainapp/contact.html', context)


def product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    title = product.name

    context = {
        'title': title,
        'links_menu': ProductCategory.objects.filter(is_active=True),
        'product': get_object_or_404(Product, pk=pk),
    }

    return render(request, 'mainapp/product.html', context)
