# Generated by Django 2.0.1 on 2020-07-22 06:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Items', '0006_customers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customers',
            name='customer_status',
        ),
    ]
