# Generated by Django 4.1.5 on 2023-01-06 08:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_orderform_text'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderform',
            options={},
        ),
        migrations.AlterField(
            model_name='orderform',
            name='order_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Register date'),
        ),
        migrations.AlterField(
            model_name='orderform',
            name='text',
            field=models.TextField(blank=True, null=True, verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='orderform',
            name='user_email',
            field=models.EmailField(blank=True, max_length=100, null=True, unique=True, validators=[django.core.validators.EmailValidator], verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='orderform',
            name='user_name',
            field=models.CharField(max_length=50, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='orderform',
            name='user_phone',
            field=models.CharField(blank=True, max_length=12, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number format: '+999999999'. Up to 12 digits allowed.", regex='^\\+?1?\\d{9,12}$')], verbose_name='Phone'),
        ),
    ]
