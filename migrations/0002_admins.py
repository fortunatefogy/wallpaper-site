# Generated by Django 4.1.5 on 2023-01-14 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='admins',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]
