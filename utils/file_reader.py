#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
from objects.page import *
from properties.properties import *


class FileReader(object):
    """File Read utility
    """
    
    @staticmethod
    def get_word_list(file_path):
        """get word list from file
        """
        f = io.open(file_path, 'r')
        word_list = f.readlines()
        f.close()
        return word_list

    @staticmethod
    def write_word_results(object_list):
        """write page information to a file
        """
        file_name = properties['search_word']
        f = io.open('files/' + file_name + '.txt', 'w')
        for obj in object_list:
            line = obj._link + ' ' + obj._title + ' ' + obj._snippet + '\n'
            f.write(line)
        f.close()
        
        

        
        
