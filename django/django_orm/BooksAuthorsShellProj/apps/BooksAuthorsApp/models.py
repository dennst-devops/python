from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class Authors(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    notes = models.TextField(max_length=255)
    books = models.ManyToManyField(Book, related_name="books_id")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"{self.first_name,  self.last_name}"