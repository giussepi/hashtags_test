# -*- coding: utf-8 -*-
""" apps documents_analizer admin """


from django.contrib import admin

from .models import Document, Hashtag


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    """ Document admin model """
    pass


@admin.register(Hashtag)
class HashtagAdmin(admin.ModelAdmin):
    """ Hashtag admin model """
    # filter_horizontal = ('documents', )
    raw_id_fields = ('documents', )
