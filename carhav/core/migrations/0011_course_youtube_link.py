# Generated by Django 3.2.16 on 2022-11-16 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20221116_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='youtube_link',
            field=models.CharField(default='', help_text='enter a promotional video link', max_length=255, verbose_name='Youtube Link'),
        ),
    ]
