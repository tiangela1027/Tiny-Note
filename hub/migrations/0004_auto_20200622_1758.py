# Generated by Django 3.0.7 on 2020-06-23 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0003_stamp_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stamp',
            name='mood',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='stamp',
            name='notes',
            field=models.CharField(max_length=264),
        ),
    ]
