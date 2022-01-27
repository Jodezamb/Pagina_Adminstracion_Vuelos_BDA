from django.db import models

# Create your models here.
class Vuelo(models.Model):
    flightId=models.AutoField(primary_key=True)
    flightsource=models.CharField(max_length=100,verbose_name='Vuelo estado')	
    flightdest=models.TextField(max_length=100,verbose_name='destino')	
    flightdate=models.DateTimeField(null=True,verbose_name='fecha')
    flightseat=models.IntegerField(null=True,verbose_name='asiento')
    ticketcost=models.FloatField(null=True,verbose_name='precio')
