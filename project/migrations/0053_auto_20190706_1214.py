# Generated by Django 2.0.13 on 2019-07-06 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0052_auto_20190705_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pro_stat',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Project'),
        ),
        migrations.AlterField(
            model_name='protags',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Project'),
        ),
        migrations.AlterField(
            model_name='userpro',
            name='project',
            field=models.ManyToManyField(to='project.Project'),
        ),
    ]
