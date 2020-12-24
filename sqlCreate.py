#!/usr/bin/env python
# coding: utf-8

# In[13]:


import xml.etree.cElementTree as ET
from collections import defaultdict
import pprint
import re
import csv
import codecs
import schema
import sqlite3 
import pandas as pd

lower = re.compile(r'^([a# ref https://stackoverflow.com/questions/50735349/import-csv-into-sqlite3-insert-failed
conn=sqlite3.connect('Seattle.db')
cur = conn.cursor() 

cur.execute('''DROP TABLE IF EXISTS nodes''')
cur.execute('''DROP TABLE IF EXISTS nodes_tags''')
cur.execute('''DROP TABLE IF EXISTS ways''')
cur.execute('''DROP TABLE IF EXISTS ways_tags''')
cur.execute('''DROP TABLE IF EXISTS ways_nodes''')


cur.execute("CREATE TABLE nodes ( id INTEGER PRIMARY KEY NOT NULL, lat REAL, lon REAL,    user TEXT, uid INTEGER, version INTEGER, changeset INTEGER, timestamp TEXT )")
conn.commit()
node_df = pd.read_csv('nodes.csv', dtype=object)
node_df.to_sql('nodes', conn, if_exists='append', index=False)


cur.execute("CREATE TABLE nodes_tags (    id INTEGER,    key TEXT,    value TEXT,    type TEXT,    FOREIGN KEY (id) REFERENCES nodes(id))")
conn.commit()
nodetag_df=pd.read_csv('nodes_tags.csv')
nodetag_df.to_sql('nodes_tags', conn, if_exists='append', index=False)

cur.execute("CREATE TABLE ways (    id INTEGER PRIMARY KEY NOT NULL,    user TEXT,    uid INTEGER,    version TEXT,    changeset INTEGER,    timestamp TEXT)")
conn.commit()
way_df=pd.read_csv('ways.csv')
way_df.to_sql('ways', conn, if_exists='append', index=False)

cur.execute("CREATE TABLE ways_nodes (    id INTEGER NOT NULL,    node_id INTEGER NOT NULL,     position INTEGER NOT NULL,     FOREIGN KEY (id) REFERENCES ways(id),    FOREIGN KEY (node_id) REFERENCES nodes(id))")
conn.commit()
waynode_df=pd.read_csv('ways_nodes.csv')
waynode_df.to_sql('ways_nodes', conn, if_exists='append', index=False)


cur.execute("CREATE TABLE ways_tags (    id INTEGER NOT NULL,    key TEXT NOT NULL,    value TEXT NOT NULL,    type TEXT,    FOREIGN KEY (id) REFERENCES ways(id))")
conn.commit()
waytag_df=pd.read_csv('ways_tags.csv')
waytag_df=waytag_df.dropna(subset=['id', 'key', 'value'], how='any')
waytag_df.to_sql('ways_tags', conn, if_exists='append', index=False)-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&;\'"\?%#$@\,\. \t\r\n]')


def key_type(element, keys):
    if element.tag == "tag":
            if lower.search(element.attrib['k']) != None: 
                keys['lower'] += 1
            elif lower_colon.search(element.attrib['k']) != None:
                keys['lower_colon'] += 1
            elif problemchars.search(element.attrib['k']) != None:
                keys['problemchars'] += 1
            else: 
                keys['other'] += 1
                
        
    return keys

def process_map(file):
    keys = {"lower": 0, "lower_colon": 0, "problemchars": 0, "other": 0}
    for _, element in ET.iterparse(file):
        keys = key_type(element, keys)

    return keys
process_map('Seattle.osm')

