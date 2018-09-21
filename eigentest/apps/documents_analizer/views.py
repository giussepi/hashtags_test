# -*- coding: utf-8 -*-
""" apps documents_analizer views """

from django.views.generic import ListView

from .models import Hashtag


class HashtagsView(ListView):
    """ Displays the hashtags list with their related documents """
    model = Hashtag
    template_name = 'documents_analizer/hastagsview.html'
    paginate_by = 5
