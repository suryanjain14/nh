# Generated by Django 2.2.1 on 2019-06-05 18:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='proUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completion', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='tag',
            field=models.TextField(max_length=20, null=True),
        ),
        migrations.CreateModel(
            name='Userpro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Project')),
                ('project', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
