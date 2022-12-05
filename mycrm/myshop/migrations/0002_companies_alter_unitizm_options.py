# Generated by Django 4.1.3 on 2022-12-05 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('short_title', models.CharField(max_length=30)),
                ('inn', models.CharField(max_length=12)),
                ('address', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Организации',
                'verbose_name_plural': 'Организации',
            },
        ),
        migrations.AlterModelOptions(
            name='unitizm',
            options={'verbose_name': 'Единица измерения', 'verbose_name_plural': 'Единицы измерения'},
        ),
    ]