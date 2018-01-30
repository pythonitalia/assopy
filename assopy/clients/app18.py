# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.conf import settings
from lxml import etree
from python_18app.api import API as App18API
from zeep import Plugin
from zeep.plugins import HistoryPlugin

configuration = getattr(settings, 'APP18_CONFIG', {})


class LoggingPlugin(Plugin):

    def ingress(self, envelope, http_headers, operation):
        print(etree.tostring(envelope, pretty_print=True))
        return envelope, http_headers

    def egress(self, envelope, http_headers, operation, binding_options):
        print(etree.tostring(envelope, pretty_print=True))
        return envelope, http_headers


def app18_client(plugins=None):
    history = HistoryPlugin()
    if plugins:
        if settings.DEBUG:
            plugins.append(LoggingPlugin())
        plugins.append(history)
    configuration['plugins'] = plugins
    return App18API(**configuration)
