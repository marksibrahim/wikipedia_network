
#loop through entries in dictionary
#traverse adding +1
#stop once already traversed or dead


import json, gc, sys

net_path = "/users/m/s/msibrahi/v3/results/flnetwork/fldict.json"

with open(net_path) as f:
    fldict = json.load(f)


#tdict = {page: clicks, cycle length, end page}

def get_fl(fldict, title):
    """adjusts case until title is a valid key, returns fl"""
    #try as is
    try:
        fl = fldict[title]
    except:
    #capitalize first letter only
        try:
            fl = fldict[title[0].upper() + title[1:]]
        except:
    #try title case
            try:
                fl = fldict[title.title()]
            except:
                fl = ""
    return fl
            
def test_traverse(fldict, start, n):
    fl = get_fl(fldict, start)
    for i in range(n):
        print fl
        if fl == "": break
        fl = get_fl(fldict, fl)
        
def correct_cap(fldict, title):
    """returns properly capitalized key, blank otherwise"""
    try:
        fl = fldict[title]
        return title
    except:
    #capitalize first letter only
        try:
            fl = fldict[title[0].upper() + title[1:]]
            return title[0].upper() + title[1:]
        except:
    #try title case
            try:
                fl = fldict[title.title()]
                return title.title()
            except KeyError:
                return ""
                

    
def traverse(fldict, start):
    """traverses first link network until repeated link (or dead)
    returns tdict: {page: clicks, cycle length, end page}"""
    gc.collect() #memory
    links_traversed = [] #change to set?
    fl = get_fl(fldict, start)
    i = 0 
    while fl not in links_traversed and fl != "":
        i +=1
        if i > 10000: #limit to 10000 traverses
            fl = "exceeded 10000 click limit"
            break
        fl = correct_cap(fldict, fl)
        links_traversed.append(fl)
        #add +1 click
        clicks = tdict.get(fl, [0,0,""])[0] + 1
        tdict[fl] = [clicks, tdict.get(fl, [0,0,""])[1], tdict.get(fl, [0,0,""])[2]]
        #next click    
        fl = get_fl(fldict, fl)
    #store cycle length and end page
    if fl == "": fl = "dead link"
    tdict[start] = [tdict.get(start, [0,0,""])[0],len(links_traversed), fl]
        

#read specified json
file_num = int(sys.argv[1])
in_path = "/users/m/s/msibrahi/v3/results/flnetwork/" + str(file_num) + ".json"


with open(in_path) as f:
    jdict = json.load(f)
    
#loop through specified json
tdict = {}
i = 0

for k in jdict.iterkeys():
    i +=1
    if i > 1000: break
    if i % 10000 == 0: print i
    traverse(fldict,k)

out_path = "/user/ms/s/msibrahi/v3/results/tdict/tdict" + str(file_num) + ".json"
with open(out_path, 'w') as outfile:
    json.dump(tdict, outfile)
