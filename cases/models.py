from django.db import models


class DotaSet(models.Model):
    RARITY_CHOICES = [
        ('Common', 'Common'),
        ('Rare', 'Rare'),
        ('Immortal', 'Immortal'),
        ('Arcana', 'Arcana'),
    ]
    name = models.CharField(max_length=100)
    hero = models.CharField(max_length=50)
    rarity = models.CharField(max_length=20, choices=RARITY_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField(max_length=500)

    def __str__(self):
        return f"{self.name} ({self.hero})"


class Case(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField(max_length=500)

    def __str__(self):
        return self.name


class CaseItem(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='items')
    dota_set = models.ForeignKey(DotaSet, on_delete=models.CASCADE)
    drop_chance = models.FloatField()
