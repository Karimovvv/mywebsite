# Generated by Django 5.1.4 on 2024-12-24 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
