# Generated by Django 3.1.2 on 2020-11-05 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201105_1314'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='name_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='name_fi',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='name_fr',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='name_sv',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
