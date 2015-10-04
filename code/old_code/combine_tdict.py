# coding: utf-8

#load all dictionaries into memory
#load fldict into memory

#loop through fldict, building master tdict

import json, gc


#load

#fldict
net_path = "/users/m/s/msibrahi/v3/results/flnetwork/fldict.json"
with open(net_path) as f:
    fldict = json.load(f)
    

#load ntdict
ntdict_path = "/users/m/s/msibrahi/v3/results/tdict/"
ntdict_names = ["tdict"+str(i)+".json" for i in range(0, 112)]
ntdict_list = []

for ntdict_name in ntdict_names:
    with open(ntdict_path + ntdict_name) as f:
        ntdict_list.append(json.load(f))




#tdict = {page: clicks, cycle length, end page}
tdict = {}


def update_tdict(page, n):
    """updates tdict with entry from nth tdict"""
    ntdict = ntdict_list[n]
    clicks, cycle_length, end_page = ntdict.get(page,[0,0,""])
    
    #update 
    clicks = clicks + tdict.get(page,[0])[0]
    cycle_length = cycle_length + tdict.get(page,[0,0])[1]
    end_page = end_page + tdict.get(page, [0,0,""])[2]
    
    #assign
    tdict[page] = [clicks, cycle_length, end_page]


#loop through fldict
i = 0
for page in fldict.iterkeys():
    i += 1
    if i > 100: break
    if i % 1000 == 0: gc.collect() #memory
    
    for n in range(0,112):
        update_tdict(page,n)



#write tdict
with open(ntdict_path + "tdict.json", 'w') as outfile:
    json.dump(tdict, outfile)




