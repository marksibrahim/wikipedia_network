
# coding: utf-8

# In[20]:

#create smallaa.xml with proper pages tags

import string, os


# In[20]:




# In[21]:

data_path = "/users/m/s/msibrahi/full_wiki_data/"

xml_write_file = data_path + "smallee"
xml_file = data_path + "smallef.xml"

cut_off = ""
with open(xml_file, 'r') as f:
    for line in f:
        cut_off = cut_off + line
        if "</page>" in line:
            break

#append lines
with open(xml_write_file, 'a') as f:
    f.write(cut_off)

#rename file
os.rename(xml_write_file, xml_write_file+".xml")


# In[14]:




# In[14]:




# In[14]:




# In[ ]:



