# Generated by Django 4.2 on 2023-05-05 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_tag_order_customer_order_product_product_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Indoor', 'Indoor'), ('Out Door', 'Out Door')], max_length=250, null=True),
        ),
    ]
