from django.shortcuts import render
from django.views.generic import TemplateView

from products.models import ProductModel


class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        pizza = ProductModel.objects.filter(category__name='Pizza')
        burgers = ProductModel.objects.filter(category__name='Burgers')
        hot_dog = ProductModel.objects.filter(category__name='Hot_dog')
        lavash = ProductModel.objects.filter(category__name='Lavash')
        salad = ProductModel.objects.filter(category__name='Salad')
        drinks = ProductModel.objects.filter(category__name='Drinks')

        context = {
            'pizza': pizza,
            'burgers': burgers,
            'hot_dog': hot_dog,
            'lavash': lavash,
            'salad': salad,
            'drinks': drinks

        }
        return context
