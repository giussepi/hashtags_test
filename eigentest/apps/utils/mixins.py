# -*- coding: utf-8 -*-
""" nlp mixins """

import os

from .utils import get_most_common_words


class HashtagMixin(object):
    """ """

    def __init__(self, *args, **kwargs):
        """ 
        * Initializes the object
        * Initializes the instance variables
        """
        super().__init__(*args, **kwargs)
        self.hashtag_list = list()
        self.hashtags_per_file = 3
        self.directory_path = 'test docs'

    def extract_hashtags_from_sources(self, directory_path=None, hashtags_per_file=None):
        """ 
        Reads the files from the directory path and extracts a user defined number of
        hashtags per file saving them at hashtag_list attribute
        """
        assert isinstance(directory_path, str) or directory_path is None, \
            "directory_path must be a string"

        assert isinstance(hashtags_per_file, int) or hashtags_per_file is None, \
            "hashtags_per_file must be a integer or None"

        self.directory_path = directory_path

        if hashtags_per_file:
            self.hashtags_per_file = hashtags_per_file

        file_list = None
        for (dirpath, dirnames, filenames) in os.walk(self.directory_path):
            file_list = filenames
            break

        if not file_list:
            raise RuntimeError("The directory_path does not contain any file")

        for filename in file_list:
            with open(os.path.join(self.directory_path, filename), 'r') as f:
                common_words = get_most_common_words(
                    f.read(), self.hashtags_per_file)
                self.hashtag_list.extend(common_words)

        # removing duplicates
        self.hashtag_list = set(self.hashtag_list)

    # def
