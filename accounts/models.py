from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(
        upload_to="users/avatars/",
        null=True, # для базы
        blank=True, # для формы 
        verbose_name="Фото профиля"
    )
    birthday = models.DateField("Дата рождения", null=True)
    phone = models.CharField("Номер телефона", max_length=14,null=True)
    following = models.ManyToManyField("self", blank=True, null=True, related_name="followers", symmetrical=False)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return str(self.username)


    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def followers_count(self):
        count=self.followers.all().count()
        return count

    @property
    def following_count(self):
        return self.following.count()
                