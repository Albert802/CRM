# Generated by Django 4.2 on 2023-06-22 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0010_customer_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
