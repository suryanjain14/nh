# Generated by Django 2.2.2 on 2019-07-01 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('project', '0021_auto_20190701_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpro',
            name='current_project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Project'),
        ),
        migrations.AlterField(
            model_name='userprodetal',
            name='completion',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userprodetal',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Project'),
        ),
    ]
