# Generated by Django 2.1.10 on 2020-04-26 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='nameToShow',
            field=models.CharField(default='', max_length=50),
        ),
    ]