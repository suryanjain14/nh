# Generated by Django 2.2.2 on 2019-06-25 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0011_auto_20190606_1613'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userpro',
            old_name='users_project',
            new_name='project',
        ),
        migrations.RemoveField(
            model_name='project',
            name='user',
        ),
        migrations.AlterField(
            model_name='userpro',
            name='current_project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Project'),
        ),
    ]
