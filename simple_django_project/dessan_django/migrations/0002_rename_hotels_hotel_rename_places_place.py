# Generated by Django 4.1 on 2022-09-04 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dessan_django', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Hotels',
            new_name='Hotel',
        ),
        migrations.RenameModel(
            old_name='Places',
            new_name='Place',
        ),
    ]