# Generated by Django 4.1 on 2022-10-12 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Photobook', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photobook',
            fields=[
                ('co_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('order_number', models.CharField(max_length=500)),
                ('page_details', models.JSONField(max_length=500)),
                ('version', models.CharField(max_length=500)),
                ('created_at', models.DateField()),
                ('updated_at', models.DateField()),
            ],
        ),
    ]
