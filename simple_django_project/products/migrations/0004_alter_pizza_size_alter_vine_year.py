# Generated by Django 4.1 on 2022-09-04 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_rename_vineyear_pizza_size_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='size',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.pizza_size'),
        ),
        migrations.AlterField(
            model_name='vine',
            name='year',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.vine_year'),
        ),
    ]
