# Generated by Django 4.2.2 on 2023-07-19 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_product_productdescription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ProductCategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.category'),
        ),
    ]
