from django.db import models


class Table(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=255)
    count = models.IntegerField()
    distance = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
