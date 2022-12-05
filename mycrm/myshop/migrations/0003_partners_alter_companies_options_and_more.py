# Generated by Django 4.1.3 on 2022-12-05 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0002_companies_alter_unitizm_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('short_title', models.CharField(max_length=30)),
                ('inn', models.CharField(max_length=12)),
                ('address', models.CharField(max_length=250)),
                ('comment', models.TextField()),
            ],
            options={
                'verbose_name': 'Партнеры',
                'verbose_name_plural': 'Партнер',
            },
        ),
        migrations.AlterModelOptions(
            name='companies',
            options={'verbose_name': 'Организации', 'verbose_name_plural': 'Организация'},
        ),
        migrations.AlterModelOptions(
            name='unitizm',
            options={'verbose_name': 'Единицы измерения', 'verbose_name_plural': 'Единица измерения'},
        ),
    ]