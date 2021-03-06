# Generated by Django 2.1.7 on 2019-09-25 08:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clubs', '0002_club_permissions'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clubmeeting',
            options={'ordering': ['moment'], 'verbose_name': 'quedada'},
        ),
        migrations.RemoveField(
            model_name='club',
            name='manager',
        ),
        migrations.RemoveField(
            model_name='club',
            name='telegram_channel',
        ),
        migrations.AddField(
            model_name='club',
            name='image',
            field=models.ImageField(blank=True, help_text='Imagen para mostrar en la lista de clubes', upload_to='clubs/', verbose_name='imagen'),
        ),
        migrations.AddField(
            model_name='club',
            name='managers',
            field=models.ManyToManyField(related_name='managed_clubs', to=settings.AUTH_USER_MODEL, verbose_name='gestores'),
        ),
        migrations.AddField(
            model_name='club',
            name='telegram_group_link',
            field=models.CharField(blank=True, default='', max_length=64, verbose_name='enlace al grupo de telegram'),
        ),
        migrations.AlterField(
            model_name='club',
            name='telegram_group',
            field=models.CharField(blank=True, default='', max_length=64, verbose_name='grupo de telegram'),
        ),
    ]
