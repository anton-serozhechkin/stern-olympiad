# Generated by Django 3.0.4 on 2020-09-09 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sore', '0002_auto_20200909_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinevent',
            name='event',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sore.Event', verbose_name='Мероприятие'),
        ),
    ]