# Generated by Django 4.1.1 on 2023-06-27 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_booking'),
    ]

    operations = [
        migrations.RenameField(
            model_name='departments',
            old_name='dep_description',
            new_name='dep_decription',
        ),
        migrations.AlterField(
            model_name='booking',
            name='p_phone',
            field=models.CharField(max_length=10),
        ),
    ]
