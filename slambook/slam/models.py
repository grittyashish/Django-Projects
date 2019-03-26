from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Writer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name


class Slam(models.Model):
    title = models.CharField(max_length=60)

    #Many slams can be associated with a single person
    writer = models.ForeignKey(Writer,max_length=20, on_delete=models.CASCADE)
    fav_sports = models.CharField(max_length=20)
    pub_date = models.DateField()
    pub_time = models.TimeField()
    slam_body = models.TextField(max_length=200)

    def __str__(self):
        return {self.title}


