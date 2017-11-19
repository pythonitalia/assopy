# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.conf import settings

from python_18app.api import API as App18API

configuration = getattr(settings, 'APP18_CONFIG', {})


def app18_client():
    return App18API(**configuration)
