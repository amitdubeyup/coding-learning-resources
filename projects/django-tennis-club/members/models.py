from django.db import models


class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    # Phone numbers are NOT integers: they can have leading zeros, "+",
    # country codes, and separators. Always store them as text.
    phone = models.CharField(max_length=32, null=True, blank=True)
    joined_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
