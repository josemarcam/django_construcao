# Generated by Django 3.2.9 on 2021-12-04 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20211204_0556'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': (('can_fire_user', 'Pode Demitir Usuarios'),), 'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.RemoveField(
            model_name='user',
            name='rule',
        ),
    ]
