# Generated by Django 5.1.4 on 2024-12-25 08:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_alter_subject_name_tutor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutor',
            name='slug',
        ),
        migrations.AddField(
            model_name='tutor',
            name='subject',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='course.subject'),
        ),
        migrations.AlterField(
            model_name='course',
            name='keywords',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='subject',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
