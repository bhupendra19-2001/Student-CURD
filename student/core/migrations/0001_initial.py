# Generated by Django 5.0.2 on 2024-02-14 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.CharField(max_length=20)),
                ('sname', models.CharField(max_length=100)),
                ('semail', models.EmailField(max_length=254)),
                ('scontact', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'student',
            },
        ),
    ]
