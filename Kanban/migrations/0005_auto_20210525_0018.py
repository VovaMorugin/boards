# Generated by Django 3.2.3 on 2021-05-25 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kanban', '0004_auto_20210525_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='due_day',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
