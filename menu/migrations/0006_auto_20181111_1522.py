# Generated by Django 2.1.2 on 2018-11-11 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_auto_20181111_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='item_description',
            field=models.TextField(blank=True),
        ),
    ]
