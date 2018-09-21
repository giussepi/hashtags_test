# -*- coding: utf-8 -*-
""" apps documents_analizer apps """

from django.apps import AppConfig


class DocumentsAnalizerConfig(AppConfig):
    """ DocumentsAnalizer AppConfig """
    name = 'documents_analizer'
    verbose_name = 'Documents analizer'

    def ready(self):
        """ loading used defined signals """
        from . import signals
