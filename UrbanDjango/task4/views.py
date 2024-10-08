from django.shortcuts import render
from django.views.generic import TemplateView


def platform(request):
    Title = 'Главная страница'
    magazin = 'Магазин'
    cart = 'Корзина'

    context = {
        'Title': Title,
        'magazin': magazin,
        'cart': cart,
    }
    return render(request, 'fourth_task/platform.html', context)


def cart(request):
    Title = 'Корзина'
    context = {
        'Title': Title
    }
    return render(request, 'fourth_task/cart.html', context)


def game(request):
    Title = 'Игры'
    # game1 = 'Atomic Heart'
    # game2 = 'Cyberpunk 2077'
    # game3 = 'PayDay 2'
    context = {
        'Title': Title,
        'games': ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2']
    }
    return render(request, 'fourth_task/game.html', context)
