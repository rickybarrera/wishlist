from django.db import models
from django.urls import reverse
# Create your models here.
class Item(models.Model):
    description = models.CharField(blank=True, null=True,max_length=100)

    def get_absolute_url(self):
        return reverse('home')
        return reverse('item_delete', kwargs={ 'pk': self.id })
