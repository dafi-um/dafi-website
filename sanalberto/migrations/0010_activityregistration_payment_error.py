# Generated by Django 2.1.13 on 2020-11-11 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sanalberto', '0009_activity_registrations'),
    ]

    operations = [
        migrations.AddField(
            model_name='activityregistration',
            name='payment_error',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='error del proceso de pago'),
        ),
    ]
