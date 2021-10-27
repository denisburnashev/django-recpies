from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def omlet_calculate(request):
    edit_ing = {}
    edit_omlet = {}
    count_servings = request.GET.get('servings', None)
    if count_servings is None:
        for ingridient, amount in DATA['omlet'].items():
            ingridient = {ingridient: amount}
            edit_ing.update(ingridient)
        edit_omlet['omlet'] = edit_ing
        for edit_ingridient, edit_amount in edit_omlet.items():
            return render(request, 'calculator/index.html', context={'recipe': {edit_ingridient: edit_amount}})
    else:
        for ingridient, amount in DATA['omlet'].items():
            ingridient = {ingridient: amount * int(count_servings)}
            edit_ing.update(ingridient)
        edit_omlet['omlet'] = edit_ing
        for edit_ingridient, edit_amount in edit_omlet.items():
            return render(request, 'calculator/index.html', context={'recipe': {edit_ingridient: edit_amount}})


def pasta_calculate(request):
    edit_ing = {}
    edit_pasta = {}
    count_servings = request.GET.get('servings', None)
    if count_servings is None:
        for ingridient, amount in DATA['pasta'].items():
            ingridient = {ingridient: amount}
            edit_ing.update(ingridient)
        edit_pasta['pasta'] = edit_ing
        for edit_ingridient, edit_amount in edit_pasta.items():
            return render(request, 'calculator/index.html', context={'recipe': {edit_ingridient: edit_amount}})
    else:
        for ingridient, amount in DATA['pasta'].items():
            ingridient = {ingridient: amount * int(count_servings)}
            edit_ing.update(ingridient)
        edit_pasta['pasta'] = edit_ing
        for edit_ingridient, edit_amount in edit_pasta.items():
            return render(request, 'calculator/index.html', context={'recipe': {edit_ingridient: edit_amount}})

def buter_calculate(request):
    edit_ing = {}
    edit_buter = {}
    count_servings = request.GET.get('servings', None)
    if count_servings is None:
        for ingridient, amount in DATA['buter'].items():
            ingridient = {ingridient: amount}
            edit_ing.update(ingridient)
        edit_buter['buter'] = edit_ing
        for edit_ingridient, edit_amount in edit_buter.items():
            return render(request, 'calculator/index.html', context={'recipe': {edit_ingridient: edit_amount}})
    else:
        for ingridient, amount in DATA['buter'].items():
            ingridient = {ingridient: amount * int(count_servings)}
            edit_ing.update(ingridient)
        edit_buter['buter'] = edit_ing
        for edit_ingridient, edit_amount in edit_buter.items():
            return render(request, 'calculator/index.html', context={'recipe': {edit_ingridient: edit_amount}})