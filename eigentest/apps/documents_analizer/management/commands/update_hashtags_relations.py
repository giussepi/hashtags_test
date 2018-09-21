# -*- coding: utf-8 -*-
""" apps documents_analizer management commands update_hashtags_relations """

from django.core.management.base import BaseCommand

from documents_analizer.models import Document, Hashtag


class Command(BaseCommand):
    """  
    Updates the relations between hashtags and documents
    """
    help = 'Updates the relations between hashtags and documents'

    def handle(self, *args, **options):
        """ 
        * Removes all Hashtags
        * Creates new Hashtags and relates them to Documents
        """
        self.stdout.write(self.style.NOTICE(
            "Updating relations between Hashtags and Documents."))

        try:
            for tag in Hashtag.objects.all():
                tag.delete()

            self.stdout.write(self.style.NOTICE("All hashtags were removed."))

            for document in Document.objects.iterator():
                document.extract_hashtags()

            self.stdout.write(self.style.SUCCESS(
                "New hashtags and relations were created successfully."))
        except Exception as e:
            self.stdout.write(self.style.ERROR(
                "Something went wrong while removing or updating the hashtags or relations."))
            self.stdout.write(self.style.ERROR(e))
