# Generated by Django 4.2.3 on 2023-07-26 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrAdmin', '0003_program_projects_alter_partne_interest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='description',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='projects',
            name='employees',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='projects',
            name='objectives',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='projects',
            name='program',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='projects',
            name='tasks',
            field=models.TextField(max_length=1000),
        ),
    ]
