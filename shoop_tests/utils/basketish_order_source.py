# -*- coding: utf-8 -*-
# This file is part of Shoop.
#
# Copyright (c) 2012-2015, Shoop Ltd. All rights reserved.
#
# This source code is licensed under the AGPLv3 license found in the
# LICENSE file in the root directory of this source tree.

from shoop.core.order_creator.source import OrderSource


class BasketishOrderSource(OrderSource):

    def __init__(self, shop):
        super(BasketishOrderSource, self).__init__(shop)
