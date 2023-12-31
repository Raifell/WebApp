# Generated by Django 4.2.6 on 2023-10-24 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('announce', models.CharField(max_length=255, verbose_name='Announce')),
                ('full_text', models.TextField(verbose_name='Text')),
                ('date', models.DateField(verbose_name='Date')),
            ],
        ),
    ]
