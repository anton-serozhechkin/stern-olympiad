# Generated by Django 2.2 on 2020-09-11 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sore', '0003_auto_20200909_1358'),
    ]

    operations = [
        migrations.CreateModel(
            name='StartOlymp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(verbose_name='Время ')),
                ('end_time', models.DateTimeField(verbose_name='Время ')),
                ('event', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sore.Event', verbose_name='Мероприятие')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sore.Student', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Время начала и окончания пользователем олимпиады',
                'verbose_name_plural': 'Время начала и окончания пользователями олимпиады',
            },
        ),
    ]
