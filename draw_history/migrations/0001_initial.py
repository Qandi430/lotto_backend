# Generated by Django 4.2.4 on 2023-08-28 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DrowHistory',
            fields=[
                ('draw_no', models.IntegerField(primary_key=True, serialize=False)),
                ('draw_no_1', models.IntegerField()),
                ('draw_no_2', models.IntegerField()),
                ('draw_no_3', models.IntegerField()),
                ('draw_no_4', models.IntegerField()),
                ('draw_no_5', models.IntegerField()),
                ('draw_no_6', models.IntegerField()),
                ('draw_date', models.DateField()),
                ('registration_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
