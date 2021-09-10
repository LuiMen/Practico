# Generated by Django 3.1.3 on 2021-09-10 02:50

from django.db import migrations, models
import prospects.validators


class Migration(migrations.Migration):

    dependencies = [
        ('prospects', '0004_prospects_reject_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prospects',
            name='rfc',
            field=models.CharField(max_length=13, validators=[prospects.validators.rfc_validator], verbose_name='rfc'),
        ),
    ]
