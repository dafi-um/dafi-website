# Generated by Django 2.1.13 on 2019-10-26 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('heart', '0009_meeting_fields'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'ordering': ('course', 'year', 'number'), 'permissions': [('can_link_group', 'Puede vincular un grupo de Telegram con un grupo de alumnos')], 'verbose_name': 'grupo'},
        ),
    ]
