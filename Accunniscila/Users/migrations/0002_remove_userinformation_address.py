# Generated by Django 2.1.10 on 2020-04-29 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinformation',
            name='address',
        ),
    ]