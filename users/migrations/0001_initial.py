# Generated by Django 3.2.9 on 2021-12-03 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('address', models.TextField()),
                ('contact', models.IntegerField()),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
