from django.db import models
from django.urls import reverse
from datetime import date

MEALS = (
    ('I', 'Insects'),
    ('S', 'Seeds'),
    ('F', 'Fruit'),
)

# Create your models here.

class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('toys_detail', kwargs={'pk': self.id})

class Finch(models.Model):
    breed = models.CharField(max_length=100)
    habitat = models.CharField(max_length=100)
    color = models.TextField(max_length=250)
    wingspan_inches = models.IntegerField()
    toys = models.ManyToManyField(Toy)

    def __str__(self):
        return f'{self.breed} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})
    
    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)
    
class Feeding(models.Model):
    MEALS = (
        ('I', 'Insects'),
        ('S', 'Seeds'),
        ('F', 'Fruit'),
    )
    date = models.DateField('feeding date')
    meal = models.CharField(max_length=1, choices=MEALS, default='I')
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_meal_display()} on {self.date}'

    class Meta:
        ordering = ('-date',) 