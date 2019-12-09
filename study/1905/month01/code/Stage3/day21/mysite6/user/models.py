from django.db import models


# Create your models here.

# file: user/models.py


class User(models.Model):
    username = models.CharField("用户名", max_length=30, unique=True)
    password = models.CharField("密码", max_length=30)

    def __str__(self):
        return "用户名" + self.username
