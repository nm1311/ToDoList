# Generated by Django 2.0.13 on 2019-02-23 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_toDoList', '0002_auto_20190223_1226'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todolist',
            old_name='item',
            new_name='item_name',
        ),
    ]
