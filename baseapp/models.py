from django.db import models

class Shop(models.Model):
    #host
    #menu
    name = models.CharField(max_length=100)
    desc = models.TextField(max_length=300, null=True, blank=True)
    covers = models.IntegerField(default=1)
    date_opened = models.DateField()
    date_closed = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=200)
    manager = models.CharField(max_length=50)
    tel_main = models.CharField(max_length=50, null=True, blank=True)
    tel_man = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

    
