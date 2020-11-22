from django.db import models
from django.utils  import timezone
from django.contrib.auth.models  import User

# Create your models here.
# 和文件上传对应的内容

class article(models.Model):
    #title
    title=models.CharField(max_length=300)
    #content
    content=models.TextField(max_length=300)

    haveurl=models.IntegerField()
    #
    url=models.TextField(max_length=300)
    def __str__(self):
        return self.title


class saQuestions(models.Model):
    #title
    title=models.CharField(max_length=300)
    #content
    content=models.TextField(max_length=300)


    #

    def __str__(self):
        return self.title
