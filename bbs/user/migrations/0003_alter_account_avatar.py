# Generated by Django 3.2.9 on 2022-03-10 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_account_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='avatar',
            field=models.CharField(default='https://s3.bmp.ovh/imgs/2022/03/5524b1bf3e53ec04.jpg', max_length=200),
        ),
    ]
