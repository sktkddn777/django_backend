from django.db import models

# Create your models here.
class Kstock(models.Model):
  name = models.CharField(max_length=100)
  purchase_data = models.DateField('when buy?')
  buy_price = models.IntegerField(default=0)
  description = models.CharField(max_length=200)
  
  def __str__(self):
    return self.name

