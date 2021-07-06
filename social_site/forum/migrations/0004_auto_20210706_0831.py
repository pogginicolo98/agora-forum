# Generated by Django 3.2.5 on 2021-07-06 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_auto_20210706_0822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='description',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Descrizione'),
        ),
        migrations.AlterField(
            model_name='section',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Immagine di copertina'),
        ),
        migrations.AlterField(
            model_name='section',
            name='name',
            field=models.CharField(max_length=80, verbose_name='Nome'),
        ),
    ]
