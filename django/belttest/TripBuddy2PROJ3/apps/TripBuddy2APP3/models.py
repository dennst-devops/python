#-#-#-#-#-#-#-#-#-#-
# TripBuddy2APP3  models.py (5)
#-#-#-#-#-#-#-#-#-#-
from django.db import models
import re
import datetime
from time import gmtime, strftime, localtime
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserValidator(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['ht_fname']) < 2:
            errors["fname"] = "First name needs to be at least 2 characters"
        if len(postData['ht_lname']) < 2:
            errors["lname"] = "Last name needs to be at least 2 characters"
        if len(postData['ht_password']) < 8:
            errors["pwlen"] = "Password needs to be at least 8 characters"
        if postData['ht_password'] != postData['ht_confpassword']:
            errors["pw"] = "Passwords do not match"
        DoesEmailExist = User.objects.filter(email=postData['ht_email']).count()
        if DoesEmailExist > 0:
            errors["exists"] = "User already exists, please login or choose a different email to use."
        if not EMAIL_REGEX.match(postData['ht_email']):
            errors['e_mail'] = ("Invalid email address!")
        return errors

    def login_validator(self, postData):
        errors = {}
        if not EMAIL_REGEX.match(postData['ht_email']):
            errors['e_mail'] = ("Invalid email address!")
            return errors
        user = User.objects.filter(email=postData['ht_email'])
        #still get a list back
        if len(user) == 0:
            errors['user'] = ("Email address is not registered! Please register.")
        else:
            logged_user = user[0]
            if not bcrypt.checkpw(postData['ht_password'].encode(), logged_user.password.encode()):
                errors['pw'] = ("Invalid password!")
        return errors

class TripValidator(models.Manager):
    def trip_validator(self, postData):
        errors = {}
        if len(postData['ht_dest']) < 3:
            errors["mydest"] = "The destination needs to be at least 3 characters"
        if len(postData['ht_start']) != 10:
            errors["stdate"] = "Please enter a valid start date"
        if len(postData['ht_end']) != 10:
            errors["edate"] = "Please enter a valid end date"
        if len(postData['ht_plan']) < 3:
            errors["myplan"] = "The plan needs to be at least 3 characters"
        #date validations go here
        return errors

    def edit_trip_validator(self, postData):
        errors = {}
        if len(postData['ht_dest']) == 1 or len(postData['ht_dest']) == 2:
            errors["mydest"] = "The destination needs to be at least 3 characters"
        if len(postData['ht_start']) >= 1 and len(postData['ht_start']) < 10:
            errors["stdate"] = "Please enter a valid start date"
        if len(postData['ht_end']) >= 1 and len(postData['ht_end']) < 10:
            errors["edate"] = "Please enter a valid end date"
        if len(postData['ht_plan']) == 1 or len(postData['ht_plan']) == 2:
            errors["myplan"] = "The plan needs to be at least 3 characters"
        #date validations go here
        return errors

class User(models.Model):
    fname = models.TextField(max_length=255)
    lname = models.TextField(max_length=255)
    email = models.TextField(max_length=255)
    password = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # trips_made
    objects = UserValidator()

class Trip(models.Model):
    dest = models.CharField(max_length=255)
    start = models.DateField(null=True)
    end = models.DateField(null=True)
    plan = models.CharField(max_length=255)
    tripmaker = models.ForeignKey(User, related_name="trips_made")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TripValidator()