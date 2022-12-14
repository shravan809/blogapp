from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=50,null=True)
    blog=models.TextField(max_length=5000,null=True)

    def __str__(self):
        return self.title
class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email
