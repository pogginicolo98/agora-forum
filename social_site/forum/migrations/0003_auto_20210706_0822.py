# Generated by Django 3.2.5 on 2021-07-06 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20210705_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='description',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='name',
            field=models.CharField(max_length=80),
        ),
    ]