# Generated by Django 5.0.1 on 2024-02-23 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aspecthomesapp', '0009_alter_requirement_virtual'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requirement',
            name='virtual',
            field=models.ImageField(null=True, upload_to='360userimages'),
        ),
    ]