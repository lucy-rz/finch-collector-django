from django.db import models
from django.urls import reverse

# Create your models here.

class Finch(models.Model):
    breed = models.CharField(max_length=100)
    habitat = models.CharField(max_length=100)
    color = models.TextField(max_length=250)
    wingspan_inches = models.IntegerField()

    def __str__(self):
        return self.breed
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})
    
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