
# coding: utf-8

# In[20]:

#create smallaa.xml with proper pages tags

import string, os


# In[20]:




# In[21]:

#construct list of 100 files
letter_range = ["a", "b", "c", "d"]
file_list = [a + b for a in ["small" + a for a in letter_range] for b in list(string.ascii_lowercase)]
extra_files = ["small" + a for a in ["ea", "eb", "ec", "ed", "ee", "ef", "eg", "eh"]]

full_file_list = file_list + extra_files


#data location
data_path = "/Users/mark/Desktop/wiki_split/"
data_path = "/Volumes/mark external/wikipedia/clean_small/"
data_path = "/users/m/s/msibrahi/full_wiki_data/"

for file_num in range(len(full_file_list)):
    #get lines
    xml_file = data_path + full_file_list[file_num+1]
    cut_off = ""
    with open(xml_file, 'r') as f:
        for line in f:
            cut_off = cut_off + line
            if "</page>" in line:
                break

    #append lines
    xml_write_file = data_path + full_file_list[file_num]
    with open(xml_write_file, 'a') as f:
        f.write(cut_off)
    
    #rename file
    os.rename(xml_write_file, xml_write_file+".xml")


# In[14]:




# In[14]:




# In[14]:




# In[ ]:



