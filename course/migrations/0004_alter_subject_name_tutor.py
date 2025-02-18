# Generated by Django 5.1.4 on 2024-12-24 09:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=500)),
                ('image', models.ImageField(upload_to='images/')),
                ('slug', models.SlugField(unique=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.subject')),
            ],
        ),
    ]
