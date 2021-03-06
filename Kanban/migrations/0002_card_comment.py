# Generated by Django 3.2.3 on 2021-05-24 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Kanban', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('due_day', models.DateTimeField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Kanban.list')),
            ],
            options={
                'verbose_name': 'card',
                'verbose_name_plural': 'cards',
                'db_table': 'cards',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField()),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Kanban.card')),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
                'db_table': 'comments',
            },
        ),
    ]
