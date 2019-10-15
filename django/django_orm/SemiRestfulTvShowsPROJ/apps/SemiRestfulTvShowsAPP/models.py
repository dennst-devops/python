from django.db import models
import re
import datetime
from time import gmtime, strftime, localtime


class ShowValidator(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['ht_title']) < 2:
            errors["title"] = "Show title should be at least 2 characters"
        if len(postData['ht_network']) < 3:
            errors["network"] = "Network name should be at least 3 characters"
        if postData['ht_reldate'] > strftime("%Y-%m-%d", localtime()):
            errors["date"] = "Release date needs to be before today"
        if len(postData['ht_desc']) < 10 and len(postData['ht_desc']) > 1: 
            errors["desc"] = "Show description should be at least 10 characters"
        DoesShowExist = Show.objects.filter(title=postData['ht_title']).count()
        print(DoesShowExist)
        if DoesShowExist > 0:
            errors["exists"] = "Show already exists"
        return errors


# Create your models here.
class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.TextField(max_length=255)
    desc = models.CharField(max_length=255)
    release_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowValidator()
