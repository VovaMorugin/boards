# Generated by Django 3.2.3 on 2021-05-25 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kanban', '0002_card_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='due_day',
            field=models.DateTimeField(null=True),
        ),
    ]
