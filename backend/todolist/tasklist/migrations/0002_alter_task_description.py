# Generated by Django 5.1.3 on 2024-11-06 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasklist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
