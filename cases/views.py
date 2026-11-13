import random
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Case
from inventory.models import UserInventory


def index(request):
    return render(request, 'cases/index.html', {'cases': Case.objects.all()})


def case_detail(request, case_id):
    return render(request, 'cases/detail.html', {'case': get_object_or_404(Case, id=case_id)})


@login_required
def open_case(request, case_id):
    if request.method != 'POST':
        return JsonResponse({'error': 'Неверный метод запроса'}, status=400)

    case = get_object_or_404(Case, id=case_id)
    if request.user.balance < case.price:
        return JsonResponse({'error': 'Недостаточно средств на балансе!'}, status=400)

    request.user.balance -= case.price
    request.user.save()

    items = list(case.items.all())
    won_item = random.choices(items, weights=[i.drop_chance for i in items], k=1)[0]
    UserInventory.objects.create(user=request.user, dota_set=won_item.dota_set)

    return JsonResponse({
        'set_name': won_item.dota_set.name,
        'hero': won_item.dota_set.hero,
        'rarity': won_item.dota_set.rarity,
        'price': float(won_item.dota_set.price),
        'image_url': won_item.dota_set.image_url,
        'new_balance': float(request.user.balance)
    })
