# Generated by Django 3.1 on 2020-09-02 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=100),
        ),
    ]
