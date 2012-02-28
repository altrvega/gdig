#!/usr/bin/env python
# -*- coding: utf-8 -*-

import simplejson as json
from properties.properties import *
from objects.page import *
from apiclient.discovery import build


class Google(object):
    """ Gets search results
    """
    
    def __init__(self):
        """
        """
        self.json_results = []
        self.object_results = None

    def do_process(self):
        startInd = 1
        while True:
            if ((startInd + 9) <= properties['page_count']):
                bulkCount = 10
                result = self.call_api(properties['search_word'], startInd, bulkCount)
                self.json_results.append(result['items'])
            else:
                bulkCount = properties['page_count'] - startInd
                if (bulkCount > 0):
                    result = self.call_api(properties['search_word'], startInd, bulkCount)            
                    self.json_results.append(result['items'])
                break
            startInd = startInd + 10

    def call_api(self, WORD, startInd, bulkCount):
        service = build("customsearch", "v1",
                        developerKey=properties['dev_key'])
        res = service.cse().list(
            q=WORD,
            cx=properties['cx'],
            num=bulkCount,
            lr=properties['lang'],
            start=startInd
            ).execute()
        return res

    def get_json_results(self):
        if not self.json_results:
            self.do_process()
            return self.json_results

    def get_object_results(self):
        if not self.json_results:
            self.do_process()
        results = []
        for res  in self.json_results:
            for item in res:
                obj = Page(item['link'], item['title'], item['snippet'])
                results.append(obj)
        return results
                
        
