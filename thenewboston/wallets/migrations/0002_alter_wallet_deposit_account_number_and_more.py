# Generated by Django 5.2.1 on 2025-05-25 21:48

from django.db import migrations, models

import thenewboston.general.validators


class Migration(migrations.Migration):

    dependencies = [
        ('wallets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='deposit_account_number',
            field=models.CharField(
                blank=True,
                max_length=64,
                null=True,
                validators=[thenewboston.general.validators.HexStringValidator(64)]
            ),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='deposit_balance',
            field=models.PositiveBigIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='deposit_signing_key',
            field=models.CharField(
                blank=True,
                max_length=64,
                null=True,
                validators=[thenewboston.general.validators.HexStringValidator(64)]
            ),
        ),
    ]
