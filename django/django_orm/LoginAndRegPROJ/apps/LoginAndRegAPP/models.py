from django.db import models
import re
import datetime
from time import gmtime, strftime, localtime
import bcrypt

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
        if len(postData['ht_password']) < 8:
            errors["pwlen"] = "Password needs to be at least 8 characters"
        if postData['ht_password'] != postData['ht_confpassword']:
            errors["pw"] = "Passwords do not match"
        DoesEmailExist = User.objects.filter(email=postData['ht_email']).count()
        if DoesEmailExist > 0:
            errors["exists"] = "User already exists"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['ht_email']):
            errors['e_mail'] = ("Invalid email address!")
        return errors

    def login_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['ht_email']):
            errors['e_mail'] = ("Invalid email address!")
            return errors
        user = User.objects.filter(email=postData['ht_email'])
        if not user: 
            errors['user'] = ("Invalid email address!")
        logged_user = user[0]
        if not bcrypt.checkpw(postData['ht_password'].encode(), logged_user.password.encode()):
            errors['pw'] = ("Invalid password!")
        return errors

# Create your models here.
class User(models.Model):
    fname = models.TextField(max_length=255)
    lname = models.TextField(max_length=255)
    email = models.TextField(max_length=255)
    password = models.TextField(max_length=255)
    # bday = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserValidator()
