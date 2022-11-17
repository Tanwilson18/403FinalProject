# Generated by Django 4.1.2 on 2022-11-16 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trailsapp', '0002_alter_menu_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='trails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trail_id', models.IntegerField()),
                ('trail_name', models.CharField(max_length=50)),
                ('length_miles', models.FloatField()),
                ('difficulty', models.CharField(max_length=15)),
                ('completion_time', models.CharField(max_length=15)),
                ('img_url', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('location', models.CharField(max_length=75)),
            ],
        ),
        migrations.DeleteModel(
            name='item',
        ),
        migrations.DeleteModel(
            name='menu',
        ),
    ]
