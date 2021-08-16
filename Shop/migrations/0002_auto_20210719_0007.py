# Generated by Django 3.2.4 on 2021-07-18 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Product_Available',
            field=models.IntegerField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='Product_Description',
            field=models.CharField(max_length=500),
        ),
    ]