# -*- coding: utf-8 -*-
""" apps documents_analizer templatetags hashtag_tags """

import re

from django import template

from ..models import Hashtag
from utils.utils import sanitize_string


register = template.Library()


@register.filter(name='print_related_docs')
def print_related_docs(object):
    """ Returns an unordered html list of all the documents related to the hashtag """
    assert isinstance(object, Hashtag)

    return "<ul>{}</ul>".format(
        "".join("<li>{}</li>".format(doc) for doc in object.documents.all()))


@register.filter(name='print_sentences_with_hashtags')
def print_sentences_with_hashtags(object):
    """ Returns an unordered html list of all the sentences containing the hashtag """
    assert isinstance(object, Hashtag)

    highlighted_lines = []
    for doc in object.documents.all():
        for line in doc.get_lines_from_source():
            cleaned_line = sanitize_string(line)
            pattern = re.compile(
                r"\s{}\W*".format(object.word), flags=re.IGNORECASE)
            if re.search(pattern, cleaned_line):
                highlighted_line = re.sub(
                    pattern,
                    "<strong class='text-primary'> {} </strong>".format(
                        object.word),
                    cleaned_line
                )
                highlighted_lines.append(highlighted_line)

    return "<ul>{}</ul>".format(
        "".join("<li>{}</li>".format(doc) for doc in highlighted_lines))
