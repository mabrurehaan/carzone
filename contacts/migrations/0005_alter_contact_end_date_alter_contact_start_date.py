# Generated by Django 4.1.1 on 2022-09-24 09:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_alter_contact_requisition_form'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='end_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='contact',
            name='start_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
