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

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return str(self.username)


    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"



class Follow(models.Model):
    to_user = models.ForeignKey(User, related_name="followers", on_delete=models.CASCADE)
    from_user = models.ForeignKey(User, related_name="follows", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
        ordering = ["-created"]

    def __str__(self):
        return f"{self.from_user} подписался на {self.to_user}" 

