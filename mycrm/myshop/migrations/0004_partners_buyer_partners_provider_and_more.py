# Generated by Django 4.1.3 on 2022-12-05 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0003_partners_alter_companies_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='partners',
            name='buyer',
            field=models.BooleanField(blank=True, default=True, verbose_name='Покупатель'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='partners',
            name='provider',
            field=models.BooleanField(blank=True, default=True, verbose_name='Поставщик'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='partners',
            name='comment',
            field=models.TextField(blank=True),
        ),
    ]
