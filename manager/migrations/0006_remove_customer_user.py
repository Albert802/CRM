# Generated by Django 4.2 on 2023-06-21 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0005_customer_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
    ]