
##Dump

You can download enwiki2015--.xml, which is 120 gb dump.

I've chopped and processed the dump into 100 pieces:
smallxx.xml 

These pieces are stored on the vacc inside fullwikidata.


##Create First Link Network

1. create_fln.py [i] 
    * i in range(0, 112)
this creates 100 json files containing the first link network

2. combine json files: use combine_fln.py
    * load all into memory at once

##Analyze First Link Network

1. Create Paths : dictionary with page --> [link1, link2, link3]
    * 100 files in paths directory

    * Compute Clicks at same time
