# Generated by Django 3.0.4 on 2020-03-25 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_remove_summary_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='summary',
            name='summary',
            field=models.BooleanField(null=True),
        ),
    ]
