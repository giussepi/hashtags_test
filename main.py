# -*- coding: utf-8 -*-
""" main  """


from apps.nlp.utils import sanitize_string, remove_stop_words, get_most_common_words
from apps.nlp.mixins import HashtagMixin

# python -m nltk.downloader -d /usr/local/share/nltk_data all
# python -m nltk.downloader -d env/share/nltk_data stopwords punkt gutenberg genesis inaugural nps_chat webtext treebank

# https://www.geeksforgeeks.org/removing-stop-words-nltk-python/

# http://www.nltk.org/book/ch01.html
# >>> fdist1 = FreqDist(text1)
# >>> print(fdist1)
# <FreqDist with 19317 samples and 260819 outcomes>
# >>> fdist1.most_common(50)


# COMMON_WORDS_PER_FILE = 5
# maybe the best way is analyzing each text separately,
# creating a list with all the words and the times they're repeated
# sort the list and select a used defined number of most common words
# This approach is justified by the fact that most common words could
# have different number of repetitions based on the lenght of the text

# for each source:
#   clean it from articles, prepositions, punctuation signals, etc
#   create a list with all the words and the times they appear
#   sort the list and select a user defined number of most common words and add them to the hashtags_list

# hashtags_dict = dict()
# for each word in the hashtags_list:
#   hashtags_dict[word] = dict()
#   for each source:
#     hashtags_dict[word][source] = list()
#     look for the word in each paragraph.
#       if found:
#         highlight word in paragraph
#         hashtags_dict[word][source].append(highlighted_paragraph)
#
#   for hashtag, docs in hashtags_dict.items():
#     print(
#       hashtag, docs.keys(),
#       [docs[doc].values() for doc in docs]
#     )
#   hashtags_dict.clear()


# create a list of hashtags from cleaned sources
# look for hashtags in documents and store
# hashtags_dict = {
#     'hashtag1': {
#         'document1': ['sentence1', 'sentence2', 'sentence3', ],
#         'document2': ['sentence1', 'sentence2', 'sentence3', ]
#     },
#     'hashtag2': {
#         'document1': ['sentence1', 'sentence2', 'sentence3', ],
#         'document2': ['sentence1', 'sentence2', 'sentence3', ]
#     },
# }
# print table highlighting the hashtag in each sentence


print(sanitize_string("SFE 324 ,, ,432 ew rw rrew$@!#F@$#%FSDFGRBGBFHrtevr"))
print(remove_stop_words("This is a blue house and nothing else matters"))
print(get_most_common_words("This is a blue house and nothing else matters"))


class SimpleClass(HashtagMixin):
    """  """
    pass


sc = SimpleClass()
sc.extract_hashtags_from_sources('test docs')
print(sc.hashtag_list)
