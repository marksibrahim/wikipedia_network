
# coding: utf-8

#load all dictionaries into memory
#load fldict into memory

#loop through fldict, building master tdict

import json, gc, sys
import datetime




#load ntdict
ntdict_path = "/users/m/s/msibrahi/v3/results/tdict/intermediate/"
ntdict_names = ["tdict"+str(i)+".json" for i in range(0, 16)]
ntdict_list = []

def load_ntdict():
    for ntdict_name in ntdict_names:
        with open(ntdict_path + ntdict_name) as f:
            ntdict_list.append(json.load(f))



#tdict = {page: clicks, cycle length, end page}
tdict = {}


def update_tdict(page, n):
    """updates tdict with entry from nth tdict"""
    clicks, cycle_length, end_page = ntdict_list[n][page]
    
    #update 
    if page in tdict:
        clicks = clicks + tdict[page][0]
        cycle_length = cycle_length + tdict[page][1]
        if tdict[page][2] not in end_page:
            end_page = end_page + tdict[page][2]
        
    #assign
    tdict[page] = [clicks, cycle_length, end_page.strip()]


#loop through tdict in intermediate folder
def get_keys():
    full_keys = []
    for i in range(16):
        nkeys = ntdict_list[i].keys()
        full_keys += nkeys
        full_keys = list(set(full_keys))
        if i == 5: gc.collect()
    return list(full_keys)

def loop_combine(full_keys):
    full_keys = get_keys()
    p = 0 
    for page in full_keys:
        p += 1
        #if p > 100: break
        if p % 10000 == 0: gc.collect() #memory
        
        for i in range(0,16):
            if page in ntdict_list[i]:
                update_tdict(page,i)


#write tdict
def write_tdict():
    write_path = ntdict_path + "/full_tdict.json"
    with open(write_path, 'w') as outfile:
        json.dump(tdict, outfile)

def run_show():
    #load ntdict
    load_ntdict()
    #get list of keys in intermediate
    full_keys = get_keys()
    #loop combine
    loop_combine(full_keys)
    #write
    write_tdict()

run_show()


    
#run time for 100 pages on 6th list (n=6)
    # < 1 
# '' for 10k pages
    # 1.5 minutes



#after it runs remember to do 110 and 111.json
