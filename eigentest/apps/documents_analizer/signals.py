# -*- coding: utf-8 -*-
""" app documents_analizer signals """

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Document


@receiver(
    post_save, sender=Document,
    dispatch_uid='post_save_documents_analizer_models_Document'
)
def document_post_save_handler(sender, instance, created, **kwargs):
    """ Hold the logic to be followed afte saving a document instance """
    if created:
        instance.extract_hashtags()
