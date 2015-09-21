# -*- coding: utf-8 -*-
# This file is part of Shoop.
#
# Copyright (c) 2012-2015, Shoop Ltd. All rights reserved.
#
# This source code is licensed under the AGPLv3 license found in the
# LICENSE file in the root directory of this source tree.
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from enumfields import Enum, EnumIntegerField
from filer.fields.image import FilerImageField
from jsonfield import JSONField
from parler.models import TranslatableModel, TranslatedFields

from shoop.core.fields import CurrencyField, InternalIdentifierField
from shoop.core.pricing import TaxfulPrice, TaxlessPrice


class ShopStatus(Enum):
    DISABLED = 0
    ENABLED = 1


@python_2_unicode_compatible
class Shop(TranslatableModel):
    identifier = InternalIdentifierField(unique=True)
    domain = models.CharField(max_length=128, blank=True, null=True, unique=True)
    status = EnumIntegerField(ShopStatus, default=ShopStatus.DISABLED)
    owner = models.ForeignKey("Contact", blank=True, null=True)
    options = JSONField(blank=True, null=True)
    currency = CurrencyField(default=(lambda: settings.SHOOP_HOME_CURRENCY))
    prices_include_tax = models.BooleanField(default=False)
    logo = FilerImageField(verbose_name=_('logo'), blank=True, null=True)

    translations = TranslatedFields(
        name=models.CharField(max_length=64),
        public_name=models.CharField(max_length=64)
    )

    def __str__(self):
        return self.safe_translation_getter("name", default="Shop %d" % self.pk)

    def create_price(self, value):
        """
        Create a price with given value and settings of this shop.

        Takes the ``prices_include_tax`` and ``currency`` settings of
        this Shop into account.

        :type value: decimal.Decimal
        :rtype: shoop.core.pricing.Price
        """
        if self.prices_include_tax:
            return TaxfulPrice(value, self.currency)
        else:
            return TaxlessPrice(value, self.currency)
