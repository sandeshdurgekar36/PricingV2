# Generated by Django 4.2.6 on 2023-10-07 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('V2', '0004_alter_distancepricetype_created_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distanceprice',
            name='updated_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='timemultiplierfactor',
            name='updated_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='waitingcharge',
            name='updated_time',
            field=models.DateTimeField(null=True),
        ),
    ]
