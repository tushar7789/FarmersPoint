# Generated by Django 4.0.4 on 2022-06-08 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
