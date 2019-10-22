#-#-#-#-#-#-#-#-#-#-
# BeltPrepAPP  models.py (5)
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
        if len(user) == 0:
            errors['user'] = ("Email address is not registered! Please register.")
        else:
            logged_user = user[0]
            if not bcrypt.checkpw(postData['ht_password'].encode(), logged_user.password.encode()):
                errors['pw'] = ("Invalid password!")
        return errors

class BookValidator(models.Manager):
    def book_validator(self, postData):
        errors = {}
        if len(postData['ht_title']) < 3:
            errors["mytitle"] = "The title needs to be at least 3 characters"
        if len(postData['ht_pubdate']) != 10:
            errors["mypubdate"] = "Please enter a valid publication date"
        if len(postData['ht_desc']) < 3:
            errors["mydesc"] = "The description needs to be at least 3 characters"
        return errors

    def edit_book_validator(self, postData):
        errors = {}
        if len(postData['ht_title']) == 1 or len(postData['ht_title']) == 2:
            errors["mytitle"] = "The title needs to be at least 3 characters"
        if len(postData['ht_pubdate']) >= 1 and len(postData['ht_pubdate']) < 10:
            errors["mypubdate"] = "Please enter a valid publication date"
        if len(postData['ht_desc']) == 1 or len(postData['ht_desc']) == 2:
            errors["mydesc"] = "The description needs to be at least 3 characters"
        return errors

class User(models.Model):
    fname = models.TextField(max_length=255)
    lname = models.TextField(max_length=255)
    email = models.TextField(max_length=255)
    password = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # books_made
    objects = UserValidator()

class Book(models.Model):
    title = models.CharField(max_length=255)
    publishdate = models.DateField(null=True)
    desc = models.CharField(max_length=255)
    bookmaker = models.ForeignKey(User, related_name="books_made")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookValidator()