# Generated by Django 4.2.2 on 2023-07-25 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='Customer_Phone_Number',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='order',
            name='Customer_address',
            field=models.CharField(default='', max_length=100),
        ),
    ]