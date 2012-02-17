#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from properties.properties import *
from utils.google import *

def main(options):
    set_properties(options)
    google_obj = Google()
    print google_obj.get_json_results()
    

""" if any value setted, use them"""
def set_properties(options):
    if options:
        if len(options) > 0:
            search_word = options[0]
            #search_word = unicode(search_word, 'utf-8')
            search_word = u"balık"
            properties['search_word'] = search_word
        if len(options) > 1:
            properties['page_count'] = options[1]
        if len(options) > 2:
            properties['lang'] = options[2]
    else:
        print "you must enter a search word"
        quit()

if __name__ == '__main__':
    main(sys.argv[1:])


