from django.db import models
from contacts.models import Contact

# Create your models here.

class Company(models.Model):
    company_name = models.TextField(max_length=255)
    website = models.URLfield(max_length=255)
    assigned_to = models.Foreignkey(User, on_delete=models.DO_NOTHING)
    qfl_relationship = models.TextField(man_length = 100)
        def __str__(self):
        return self.first_name + " " + self.last_name   