# Generated by Django 2.2.2 on 2019-06-26 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='groups',
            name='name',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
    ]
