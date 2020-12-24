#!/usr/bin/env python
# coding: utf-8

# In[13]:


query='''select DISTINCT value from nodes_tags where key = 'amenity'; '''

result=cur.execute(query)
for row in result:
    print (row)

