# Generated by Django 3.2.16 on 2022-11-14 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20221114_1815'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.CharField(default='', max_length=100, verbose_name='category'),
        ),
        migrations.AddField(
            model_name='course',
            name='payment_link',
            field=models.CharField(default='', max_length=255, verbose_name='payment_link'),
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='', max_length=255, verbose_name='category'),
        ),
    ]
