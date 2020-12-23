#!/usr/bin/env python
# coding: utf-8

# In[13]:


# ref https://stackoverflow.com/questions/50735349/import-csv-into-sqlite3-insert-failed
conn=sqlite3.connect('Seattle.db')
cur = conn.cursor() 
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
waytag_df.to_sql('ways_tags', conn, if_exists='append', index=False)

