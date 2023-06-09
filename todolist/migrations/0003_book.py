# Generated by Django 4.0.4 on 2023-04-05 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_alter_todo_options_alter_todo_is_complete_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1', models.CharField(max_length=150)),
                ('img', models.ImageField(upload_to='images/')),
                ('bk', models.FileField(upload_to='books/')),
            ],
        ),
    ]
