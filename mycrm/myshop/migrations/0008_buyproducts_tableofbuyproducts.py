# Generated by Django 4.1.3 on 2022-12-08 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0007_banks_bankaccount'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150)),
                ('number', models.CharField(max_length=30)),
                ('date', models.DateTimeField()),
                ('company', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='myshop.companies')),
                ('partner', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='myshop.partners')),
            ],
        ),
        migrations.CreateModel(
            name='TableOfBuyProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.FloatField()),
                ('price', models.FloatField()),
                ('summa', models.FloatField()),
                ('doc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myshop.buyproducts')),
                ('prod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myshop.goods')),
                ('unizm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myshop.unitizm')),
            ],
        ),
    ]
