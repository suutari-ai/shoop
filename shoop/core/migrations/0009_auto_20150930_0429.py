# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import shoop.core.fields
import shoop.core.models.shops


class Migration(migrations.Migration):

    dependencies = [
        ('shoop', '0008_maintenance_mode'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='taxful_total_price',
            new_name='taxful_total_price_value',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='taxless_total_price',
            new_name='taxless_total_price_value',
        ),
        migrations.RenameField(
            model_name='orderline',
            old_name='_total_discount_amount',
            new_name='total_discount_value',
        ),
        migrations.RenameField(
            model_name='orderline',
            old_name='_unit_price_amount',
            new_name='unit_price_value',
        ),
        migrations.RenameField(
            model_name='orderlinetax',
            old_name='amount',
            new_name='amount_value',
        ),
        migrations.RenameField(
            model_name='orderlinetax',
            old_name='base_amount',
            new_name='base_amount_value',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='amount',
            new_name='amount_value',
        ),
        migrations.RenameField(
            model_name='shopproduct',
            old_name='default_price',
            new_name='default_price_value',
        ),
        migrations.RenameField(
            model_name='tax',
            old_name='amount',
            new_name='amount_value',
        ),
        migrations.RemoveField(
            model_name='address',
            name='vat_code',
        ),
        migrations.RemoveField(
            model_name='companycontact',
            name='vat_code',
        ),
        migrations.RemoveField(
            model_name='order',
            name='vat_code',
        ),
        migrations.RemoveField(
            model_name='orderline',
            name='_prices_include_tax',
        ),
        migrations.RemoveField(
            model_name='product',
            name='purchase_price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='suggested_retail_price',
        ),
        migrations.RemoveField(
            model_name='suppliedproduct',
            name='purchase_price',
        ),
        migrations.RemoveField(
            model_name='suppliedproduct',
            name='suggested_retail_price',
        ),
        migrations.AddField(
            model_name='address',
            name='tax_number',
            field=models.CharField(max_length=64, verbose_name='Tax number', blank=True),
        ),
        migrations.AddField(
            model_name='companycontact',
            name='tax_number',
            field=models.CharField(max_length=32, verbose_name='Tax number (e.g. EIN in US or VAT code in Europe)', blank=True),
        ),
        migrations.AddField(
            model_name='order',
            name='currency',
            field=shoop.core.fields.CurrencyField(max_length=4, default='EUR'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='prices_include_tax',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='tax_number',
            field=models.CharField(max_length=20, verbose_name='Tax number', blank=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='foreign_amount_value',
            field=shoop.core.fields.MoneyValueField(null=True, decimal_places=9, max_digits=36, default=None, blank=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='foreign_currency',
            field=shoop.core.fields.CurrencyField(max_length=4, null=True, default=None, blank=True),
        ),
        migrations.AddField(
            model_name='shop',
            name='currency',
            field=shoop.core.fields.CurrencyField(max_length=4, default=shoop.core.models.shops._get_default_currency),
        ),
        migrations.AddField(
            model_name='tax',
            name='currency',
            field=shoop.core.fields.CurrencyField(max_length=4, null=True, default=None, blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='tax_group',
            field=models.ForeignKey(null=True, blank=True, to='shoop.CustomerTaxGroup'),
        ),
        migrations.AlterField(
            model_name='order',
            name='display_currency',
            field=shoop.core.fields.CurrencyField(max_length=4, blank=True),
        ),
        migrations.AlterField(
            model_name='shop',
            name='prices_include_tax',
            field=models.BooleanField(default=False),
        ),
    ]
