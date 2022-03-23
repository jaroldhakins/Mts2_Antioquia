from django.db import models


class valle_aburra(models.Model):
    id = models.IntegerField(primary_key=True)
    stratum = models.IntegerField()
    price = models.BigIntegerField()
    mtsC = models.IntegerField()
    description = models.CharField(max_length=255)
    barrio = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.city}, precio: {self.price}, mts2: {self.mtsC}'

class oriente(models.Model):
    id = models.IntegerField(primary_key=True)
    stratum = models.IntegerField()
    price = models.BigIntegerField()
    mtsC = models.IntegerField()
    description = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.city}, precio: {self.price}, mts2: {self.mtsC}'

class rest_antioquia(models.Model):
    id = models.IntegerField(primary_key=True)
    stratum = models.IntegerField()
    price = models.BigIntegerField()
    mtsC = models.IntegerField()
    description = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.city}, precio: {self.price}, mts2: {self.mtsC}, estrato: {self.stratum}'
