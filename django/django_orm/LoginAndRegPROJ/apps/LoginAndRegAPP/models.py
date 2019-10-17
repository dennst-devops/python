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
        if postData['ht_bday'] > strftime("%Y-%m-%d", localtime()):
            errors["date1"] = "Birthdate needs to be before today (no future dates)"
        # if postData['ht_bday'] > (int(strftime("%Y-%m-%d", localtime())) - 4745):
        #     print(int(strftime("%Y-%m-%d", localtime())))
        #     errors["date2"] = "User needs to be at least 13 years old"
            #4745 days
            #datetime.datetime.now() - datetime.timedelta(days=3*365)
            #seconds in a year: 409968000
            #mytime = datetime.datetime(int(x[0]), int(x[1]), int(x[2])).timestamp()
            #2006-10-18
        #########################
        # leaving debugging info in for date checks
        #########################
        print("*"*32)
        print(postData['ht_bday'])
        #check for a valid birthdate (no blanks)
        if len(postData['ht_bday']) != 10:
            errors["bday2"] = "Enter a valid birthdate"
        else:
            # get the date and split on -
            userbday=postData['ht_bday'].split("-")
            # break down to YYYY MM DD
            # print(userbday[0])
            # print(userbday[1])
            # print(userbday[2])
            # remove leading zeros on the month and day because the datetime.datetime function doesn't like leading zeros...
            mygoodmo=userbday[1].lstrip("0")
            mygoodday=userbday[2].lstrip("0")
            # print(mygoodmo)
            # print(mygoodday)
            # if the user was born before 1970, they're over 13. This is requred due to UNIX timestamps starting at 1970-01-01
            if int(userbday[0]) > 1970:
                thentime = datetime.datetime(int(userbday[0]), int(mygoodmo), int(mygoodday)).timestamp()
                nowtime=round(datetime.datetime.now().timestamp())
                if nowtime - thentime < 409968000:
                    errors["date2"] = "User needs to be at least 13 years old"
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

class PostingValidator(models.Manager):
    def message_validator(self, postData):
        errors = {}
        if len(postData['ht_messagetxt']) < 8:
            errors["message"] = "Message needs to be at least 8 characters long"
        return errors

    def comment_validator(self, postData):
        errors = {}
        if len(postData['ht_commenttxt']) < 8:
            errors["comment"] = "Comment needs to be at least 8 characters long"
        return errors

# Create your models here.
class User(models.Model):
    fname = models.TextField(max_length=255)
    lname = models.TextField(max_length=255)
    email = models.TextField(max_length=255)
    password = models.TextField(max_length=255)
    bday = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # messages_made
    # comments_made
    objects = UserValidator()

class PostMessage(models.Model):
    postmessage = models.TextField(max_length=2048)
    messagemaker = models.ForeignKey(User, related_name="messages_made")
    #poster related_name=posts
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # comment_to_message
    objects = PostingValidator()

class Comment(models.Model):
    comment = models.TextField(max_length=1024)
    commentmaker = models.ForeignKey(User, related_name="comments_made")
    #commenter, related_name=comments
    commenttomessage = models.ForeignKey(PostMessage, related_name="comment_to_message")
    #message, related_name=comments
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = PostingValidator()