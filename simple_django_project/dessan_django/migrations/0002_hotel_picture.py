# Generated by Django 4.1 on 2022-09-04 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dessan_django', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='picture',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]