# Generated by Django 3.2.9 on 2021-12-07 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='short_description',
            field=models.TextField(default='Descrição breve', max_length=100, verbose_name='Shprt Activity Description'),
        ),
    ]
