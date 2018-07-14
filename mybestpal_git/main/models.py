from django.db import models
from django.conf import settings

# Create your models here.


from django.db import models
from django.contrib.auth.models import User



# class updateUser(models.Model):
#     dob = models.DateField(null=True, blank=True)
#     phno=models.CharField(max_length=12,null=True)
#
#
#     dob.contribute_to_class(User, 'dob')
#     phno.contribute_to_class(User, 'phno')

class UserProfile(models.Model):
    dob = models.DateField(null=True, blank=True)
    phno=models.CharField(max_length=12,null=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)



class MyTask(models.Model):

    start_date = models.DateField(null=True, blank=True)
    start_time=models.TimeField()
    type = models.CharField(max_length=128)
    description = models.CharField(max_length=128)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


    def __str__(self):
        return self.type


class Friend(models.Model):
    userid_1=models.IntegerField()
    userid_2=models.IntegerField()

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class PasswordData(models.Model):
    username = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    account_name = models.CharField(max_length=128)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)



class BankData(models.Model):
    bankname = models.CharField(max_length=128)
    cardname = models.CharField(max_length=128)
    cardnumber = models.CharField(max_length=128)
    cvv=models.CharField(max_length=5)
    type=models.CharField(max_length=10)
    expiry=models.DateField(null=True, blank=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)





class GameInfo:

    game1=models.IntegerField()
    game2 = models.IntegerField()
    game3 = models.IntegerField()
    game4 = models.IntegerField()

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)




