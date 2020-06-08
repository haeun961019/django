from django.db import models
#68
from django.contrib.auth.models import User

# Create your models here.

class Bookmark(models.Model):
    title = models.CharField('TITLE', max_length=100, blank=True)
    url = models.URLField('URL', unique=True)
    description = models.CharField('설명,', max_length = 100, blank= True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        # return "%s %s" %(self.title,"가나다라")
        return self.title
