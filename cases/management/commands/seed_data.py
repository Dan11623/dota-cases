from django.core.management.base import BaseCommand
from cases.models import Case, DotaSet, CaseItem


class Command(BaseCommand):
    help = 'Заполняет БД начальными кейсами и сетами Dota 2'

    def handle(self, *args, **kwargs):
        Case.objects.all().delete()
        DotaSet.objects.all().delete()

        s1 = DotaSet.objects.create(
            name="BZZ Pugna Set", hero="Pugna", rarity="Common", price=35,
            image_url="https://steamstatic.com"
        )
        s2 = DotaSet.objects.create(
            name="Arms of Burning Turmoil", hero="Chaos Knight", rarity="Rare", price=140,
            image_url="https://steamstatic.com"
        )
        s3 = DotaSet.objects.create(
            name="Manifold Paradox", hero="Phantom Assassin", rarity="Arcana", price=2500,
            image_url="https://steamstatic.com"
        )
        s4 = DotaSet.objects.create(
            name="Demon Eater", hero="Shadow Fiend", rarity="Arcana", price=2200,
            image_url="https://steamstatic.com"
        )

        c1 = Case.objects.create(
            name="Сокровищница Новичка",
            description="Идеальный старт: низкая цена и реальный шанс выбить Аркану на PA или SF!",
            price=100,
            image_url="https://steamstatic.com"
        )
        c2 = Case.objects.create(
            name="Королевский Джекпот",
            description="Повышенные шансы на редкие сеты и Арканы для настоящих хайроллеров.",
            price=450,
            image_url="https://steamstatic.com"
        )

        CaseItem.objects.create(case=c1, dota_set=s1, drop_chance=60.0)
        CaseItem.objects.create(case=c1, dota_set=s2, drop_chance=30.0)
        CaseItem.objects.create(case=c1, dota_set=s3, drop_chance=5.0)
        CaseItem.objects.create(case=c1, dota_set=s4, drop_chance=5.0)

        CaseItem.objects.create(case=c2, dota_set=s2, drop_chance=60.0)
        CaseItem.objects.create(case=c2, dota_set=s3, drop_chance=20.0)
        CaseItem.objects.create(case=c2, dota_set=s4, drop_chance=20.0)

        self.stdout.write(self.style.SUCCESS('База успешно заполнена кейсами и сетами!'))
