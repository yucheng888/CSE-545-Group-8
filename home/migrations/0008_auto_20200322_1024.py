# Generated by Django 3.0.2 on 2020-03-22 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20200322_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_number',
            field=models.IntegerField(default=8244619791, max_length=10, unique=True),
        ),
    ]