# Generated by Django 2.1.13 on 2019-12-04 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heart', '0015_people_groups_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='documents',
            field=models.ManyToManyField(blank=True, to='heart.DocumentMedia', verbose_name='documentos relacionados'),
        ),
    ]
