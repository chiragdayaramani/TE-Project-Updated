from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser , BaseUserManager # change
from .manager import UserManager #chnage


class  User(models.Model):
    username = None
    email = models.EmailField(unique = True, blank=True)
    first_name  = models.CharField(max_length=100)
    last_name   =  models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    aadhar_no = models.CharField(max_length=100)
    user_type = models.CharField(max_length=100)
    test_after = models.CharField(max_length=100)
    email_token = models.CharField(max_length=100, null = True, blank = True)
    forget_password = models.CharField(max_length=100, null = True, blank = True)
    last_login = models.CharField(max_length=100, null = True, blank = True)
    last_logout = models.CharField(max_length=100, null = True, blank = True)
    password = models.CharField(max_length=100, default = "")

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    # def __str__(self):
    #     return self.email
    
class After10(models.Model):
    question=models.CharField(max_length=150,unique=True)
    question_type = models.CharField(max_length = 120,default=" ")

class After12Arts(models.Model):
    question=models.CharField(max_length=150,unique=True)

class After12Commerce(models.Model):
    question=models.CharField(max_length=150,unique=True)

class After12Science(models.Model):
    question=models.CharField(max_length=150,unique=True)

class After10colleges(models.Model):
    college_id = models.AutoField
    college_name = models.CharField(max_length=1000 ,  default="")
    college_address = models.CharField(max_length=1000 ,  default="")
    phone_number = PhoneNumberField(default="")
    website = models.URLField(max_length = 500, default="")

class After12engcolleges(models.Model):
    college_id = models.AutoField
    college_name = models.CharField(max_length=1000,  default="")
    college_address = models.CharField(max_length=1000,  default="")
    phone_number = PhoneNumberField(default="")
    website = models.URLField(max_length = 500, default="")

class After12medicolleges(models.Model):
    college_id = models.AutoField
    college_name = models.CharField(max_length=1000,  default="")
    college_address = models.CharField(max_length=1000,  default="")
    phone_number = PhoneNumberField(default="")
    website = models.URLField(max_length = 500, default="")

class After12commcolleges(models.Model):
    college_id = models.AutoField
    college_name = models.CharField(max_length=1000,  default="")
    college_address = models.CharField(max_length=1000,  default="")
    phone_number = PhoneNumberField(default="")
    website = models.URLField(max_length = 500, default="")

class After12artscolleges(models.Model):
    college_id = models.AutoField
    college_name = models.CharField(max_length=1000,  default="")
    college_address = models.CharField(max_length=1000,  default="")
    phone_number = PhoneNumberField(default="")
    website = models.URLField(max_length = 500, default="")
    
class result(models.Model):
    ans_CATEGORIES =(
        ('Dislike' , 'Dislike'),
        ('Neutral' , 'Neutral'),
        ('Enjoy' , 'Enjoy'),
       )
    result_id = models.AutoField
    # users=models.ForeignKey('User',null=True, on_delete=models.CASCADE,)
    # user_id = models.IntegerField()
    # user = User.email.EmailField(unique = True, blank=True)
    username = models.EmailField(unique = False, blank=True)
    # email = models.EmailField(unique = False, blank=True)
    question=models.CharField(max_length=1000,  default="")
    answer = models.CharField(max_length=9,choices=ans_CATEGORIES)
    question_type = models.CharField(max_length=50,default = "")

    def __str__(self):
        return self.email
    
class result12arts(models.Model):
    ans_CATEGORIES =(
        ('Dislike' , 'Dislike'),
        ('Neutral' , 'Neutral'),
        ('Enjoy' , 'Enjoy'),
       )
    result_id = models.AutoField
    # users=models.ForeignKey('User',null=True, on_delete=models.CASCADE,)
    # user_id = models.IntegerField()
    # user = User.email.EmailField(unique = True, blank=True)
    username = models.EmailField(unique = False, blank=True)
    question=models.CharField(max_length=1000,  default="")
    answer = models.CharField(max_length=9,choices=ans_CATEGORIES)

def __str__(self):
        return self.username
    
class result12comm(models.Model):
    ans_CATEGORIES =(
        ('Dislike' , 'Dislike'),
        ('Neutral' , 'Neutral'),
        ('Enjoy' , 'Enjoy'),
       )
    result_id = models.AutoField
    # users=models.ForeignKey('User',null=True, on_delete=models.CASCADE,)
    # user_id = models.IntegerField()
    # user = User.email.EmailField(unique = True, blank=True)
    username = models.EmailField(unique = False, blank=True)
    question=models.CharField(max_length=1000,  default="")
    answer = models.CharField(max_length=9,choices=ans_CATEGORIES)

def __str__(self):
        return self.username
    
class result12sci(models.Model):
    ans_CATEGORIES =(
        ('Dislike' , 'Dislike'),
        ('Neutral' , 'Neutral'),
        ('Enjoy' , 'Enjoy'),
       )
    result_id = models.AutoField
    # users=models.ForeignKey('User',null=True, on_delete=models.CASCADE,)
    # user_id = models.IntegerField()
    # user = User.email.EmailField(unique = True, blank=True)
    username = models.EmailField(unique = False, blank=True)
    question=models.CharField(max_length=1000,  default="")
    answer = models.CharField(max_length=9,choices=ans_CATEGORIES)

def __str__(self):
        return self.username
    