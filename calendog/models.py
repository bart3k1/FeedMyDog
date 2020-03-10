from django.contrib.auth.models import User
from django.db import models

FREQUENCY = (
    (1, "Once a day"),
    (2, "Twice a day"),
)


class Caretaker(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length = 254)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class AddCallendog(models.Model):
    title = models.CharField(max_length=255)
    start_date = models.DateField()
    stop_date = models.DateField()
    frequency = models.IntegerField(choices=FREQUENCY, blank=True, null=True)
    caretakers = models.ManyToManyField(Caretaker)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
