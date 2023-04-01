from django.db import models
from django.contrib.auth.hashers import make_password

class Member(models.Model):
  username = models.CharField(max_length=100, unique=True)
  password = models.CharField(max_length=100)
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  email = models.EmailField(unique=True)
  proficiency = models.CharField(max_length=20,
                               choices=[("1", "Beginner"), ("2", "Intermediate"), ("3", "Expert")],
                               default='1')
  age = models.IntegerField(null=True)
  address = models.TextField(null=True)
  contact = models.CharField(max_length=10, null=True)
  
  def __str__(self):
    return f"{self.username} {self.firstname}"
  
  def save(self, *args, **kwargs):
    self.password = make_password(self.password)
    super(Member, self).save(*args, **kwargs)