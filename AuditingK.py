#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pprint
import xml.etree.cElementTree as ET

def get_types_of_k_attrib(filename, k_attrib_values_dict):
    
    for _, element in ET.iterparse(filename):
        if element.tag == "node" or element.tag == "way":
            for tag in element.iter("tag"):
                #print(tag.attrib['k'])
                if tag.attrib['k'] not in k_attrib_values_dict:
                    k_attrib_values_dict[tag.attrib['k']] = 1
                else:
                    k_attrib_values_dict[tag.attrib['k']] += 1
                tag.clear()
            element.clear()

if __name__ == '__main__':
    
    k_attrib_values_dict = {}
    
    filename = "Seattle.osm"
    get_types_of_k_attrib(filename, k_attrib_values_dict)
    
    #print the top 10 k values appearing in the Seattle.osm file
    import operator
    pprint.pprint(sorted(k_attrib_values_dict.items(),key = operator.itemgetter(1),reverse = True)[1:11])


# In[2]:


import pprint
import re
import xml.etree.cElementTree as ET

datadir = "data"
datafile = "Seattle.osm"

lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')


def key_type(element, keys):
    if element.tag == "tag":
        for tag in element.iter('tag'):
            k = tag.get('k')
            if lower.search(k):
                keys['lower'] += 1
            elif lower_colon.search(k):
                keys['lower_colon'] += 1
            elif problemchars.search(k):
                keys['problemchars'] += 1
            else:
                keys['other'] += 1
    return keys


def process_map(filename):
    keys = {"lower": 0, "lower_colon": 0, "problemchars": 0, "other": 0}
    for _, element in ET.iterparse(filename):
        keys = key_type(element, keys)

    return keys

seattle_keys = process_map(datafile)
pprint.pprint(seattle_keys)

