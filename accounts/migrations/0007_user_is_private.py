# Generated by Django 3.2.9 on 2022-10-22 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_user_following'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_private',
            field=models.BooleanField(default=False, verbose_name='Закрытый аккаунт'),
        ),
    ]
