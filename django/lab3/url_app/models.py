from django.db import models
from django.conf import settings


#Create your models here
class Url_short(models.Model):
    code = models.CharField(max_length=15, unique=True)
    long_url = models.CharField(max_length=2000, unique=True)

    def __str__(self):
        return self.long_url


    # def create_shortcode(instance,):
    #     new_code = code_generator(size=size)
    #     return new_code
