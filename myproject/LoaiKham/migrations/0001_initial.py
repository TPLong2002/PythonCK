# Generated by Django 4.2 on 2023-05-11 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoaiKham',
            fields=[
                ('LoaiKham_id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
            ],
        ),
    ]