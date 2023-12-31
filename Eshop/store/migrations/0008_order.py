# Generated by Django 4.2.2 on 2023-07-25 16:03

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductQuantity', models.IntegerField(default=1)),
                ('Price', models.IntegerField()),
                ('date', models.DateField(default=datetime.datetime.today)),
                ('Customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.customer')),
                ('Product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
        ),
    ]
