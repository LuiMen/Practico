# Generated by Django 3.2.7 on 2021-09-07 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prospects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documents',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='prospects',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='prospects',
            name='second_lastname',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='second lastname'),
        ),
    ]
