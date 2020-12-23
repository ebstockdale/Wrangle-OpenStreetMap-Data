#!/usr/bin/env python
# coding: utf-8

# In[1]:


import xml.etree.cElementTree as ET
import pprint

OSMFILE = 'Seattle.osm'

def count_tags(filename):
    tags = {}
    for event, elem in ET.iterparse(filename):
        if elem.tag not in tags.keys():
            tags[elem.tag] = 1
        else:
            tags[elem.tag] += 1
    return tags

tags = count_tags(OSMFILE)
pprint.pprint(tags)

