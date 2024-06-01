from django.db import models


class User(models.Model):
    username = models.CharField("Username", unique=True)
    password = models.TextField("Password")
    email = models.EmailField("Email", unique=True)
    avatar = models.ImageField("Avatar", upload_to="media/avatars")

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
