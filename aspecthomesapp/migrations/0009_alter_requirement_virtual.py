# Generated by Django 5.0.1 on 2024-02-23 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aspecthomesapp', '0008_remove_bidding_designer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requirement',
            name='virtual',
            field=models.ImageField(upload_to='360userimages'),
        ),
    ]