
# coding: utf-8

#load all dictionaries into memory
#load fldict into memory

#loop through fldict, building 10 master tdict chucks
    # need to add 100, 111 tdict manually
#then run step_tdict 2 

import json, gc, sys
import datetime
import shutil



#load fldict
def load_nfldict(n):
    net_path = "/users/m/s/msibrahi/v3/results/flnetwork/"+str(n)+".json"
    with open(net_path) as f:
        fldict = json.load(f)
    return fldict

    

#load ntdict
ntdict_path = "/users/m/s/msibrahi/v3/results/tdict/"
ntdict_names = ["tdict"+str(i)+".json" for i in range(0, 112)]
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


#loop through pages in json (nfldict)  between (file_sec, +1)
def loop_combine(n):
    n = int(n)
    for ln in range(n*10,(n+1)*10):
        nfldict = load_nfldict(n)
        p = 0
        for page, v in nfldict.iteritems():
            p += 1
            #if p > 100: break
            if p % 10000 == 0: gc.collect() #memory
            
            for i in range(0,112):
                if page in ntdict_list[i]:
                    update_tdict(page,i)


#write tdict
def write_tdict(n):
    write_path = ntdict_path + "intermediate/tdict" + str(n) + ".json"
    with open(write_path, 'w') as outfile:
        json.dump(tdict, outfile)

def run_show(n):
    #load ntdict
    load_ntdict()
    ntdict_time =  str(datetime.datetime.now().time())
    #n = int(sys.argv[1])
    #loop
    loop_combine(n)
    #write
    write_tdict(n)
    finish_time =  str(datetime.datetime.now().time())

n = sys.argv[1]
run_show(n)
#move tdict110 - 114
if int(n) == 1:
#n ==1 ensures it only occurs once
    shutil.move(ntdict_path + "tdict110.json", ntdict_path + "tdict11.json")
    shutil.move(ntdict_path + "tdict111.json", ntdict_path + "tdict12.json")
    shutil.move(ntdict_path + "tdict112.json", ntdict_path + "tdict13.json")
    shutil.move(ntdict_path + "tdict113.json", ntdict_path + "tdict14.json")
    shutil.move(ntdict_path + "tdict114.json", ntdict_path + "tdict15.json")


    
#run time for 100 pages on 6th list (n=6)
    # < 1 
# '' for 10k pages
    # 1.5 minutes



#after it runs remember to do 110 and 111.json
