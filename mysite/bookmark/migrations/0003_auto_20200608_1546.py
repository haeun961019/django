# Generated by Django 3.0.7 on 2020-06-08 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0002_auto_20200604_1752'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookmark',
            name='hi',
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='description',
            field=models.CharField(blank=True, max_length=100, verbose_name='설명,'),
        ),
    ]
