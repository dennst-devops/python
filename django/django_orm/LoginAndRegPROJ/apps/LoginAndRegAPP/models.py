from django.db import models
import re
import datetime
from time import gmtime, strftime, localtime


class UserValidator(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['ht_fname']) < 2:
            errors["fname"] = "First name needs to be at least 2 characters"
        if len(postData['ht_lname']) < 2:
            errors["lname"] = "Last name needs to be at least 2 characters"
        # if postData['ht_bdate'] > strftime("%Y-%m-%d", localtime()):
        #     errors["date"] = "Birthdate needs to be before today"
        #     errors["date"] = "User needs to be at least 13 years old"
        DoesShowExist = User.objects.filter(title=postData['ht_title']).count()
        print(DoesShowExist)
        if DoesShowExist > 0:
            errors["exists"] = "Show already exists"
        return errors


# Create your models here.
class User(models.Model):
    fname = models.TextField(max_length=255)
    lname = models.TextField(max_length=255)
    email = models.TextField(max_length=255)
    password = models.TextField(max_length=255)
    bday = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserValidator()
