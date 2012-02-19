#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from properties.properties import *
from utils.google import *
from utils.file_reader import *

def main(options):
    set_properties(options)

def get_word_results():
    google_obj = Google()
    print google_obj.get_json_results()
    return google_obj.get_object_results()

def do_process():
    """ makes the main operation
    get words from file and create link files
    """
    words = FileReader.get_word_list(properties['word_file'])
    for word in words:
        word = word.split()
        properties['search_word'] = word
        object_list = get_word_results()
        FileReader.write_word_results(object_list)

""" if any value setted, use them"""
def set_properties(options):
    if options:
        if len(options) > 0:
            search_word = options[0]
            search_word = unicode(search_word, 'utf-8')
            #search_word = u"balık"
            properties['search_word'] = search_word
        if len(options) > 1:
            properties['page_count'] = options[1]
        if len(options) > 2:
            properties['lang'] = options[2]
        get_word_results()
    else:
        #if not any words given, reads wordlist from file
        do_process()

if __name__ == '__main__':
    main(sys.argv[1:])


