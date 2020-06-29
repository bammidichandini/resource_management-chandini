# Generated by Django 3.0.5 on 2020-06-05 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource_management', '0002_auto_20200605_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='access_level',
            field=models.CharField(choices=[('Read', 'Read'), ('Write', 'Write'), ('Read_and_Write', 'Read_and_Write')], max_length=50, null=True),
        ),
    ]
