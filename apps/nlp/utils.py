# -*- coding: utf-8 -*-
""" nlp utils """

# import pdb

import unidecode
from nltk.book import FreqDist
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def sanitize_string(string):
    """ 
    Returns the string lowercased, without special characters, accents or multiple
    spaces
    """
    # https://pypi.org/project/Unidecode/
    # removing accents and using lowercase letters",
    # string = unicode(string)
    string = unidecode.unidecode(string.lower().strip())
    # removing special characters"
    string = "".join(i for i in string if i.isalnum() or i == " ")
    # removing multiple spaces"
    string = " ".join(string.split())

    return string


def remove_stop_words(string):
    """ Remove all stop words and returns a list of words """
    stop_words = set(stopwords.words('english'))
    raw_words = word_tokenize(string)

    return list(filter(lambda word: word not in stop_words, raw_words))


def get_most_common_words(string, common_words_number=3):
    """ 
    * Sanitizes and removes all stop words
    * Returns a list with the most common words
    """
    cleaned_data = sanitize_string(string)
    cleaned_data = remove_stop_words(cleaned_data)
    common_words = FreqDist(cleaned_data).most_common(common_words_number)

    return [i[0] for i in common_words]
