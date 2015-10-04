"""
create a dictionary of page: loop length
includes only pages inside true loops
"""
#takes a file num and creates xpath.json

import json, gc, sys


#goal path[page] = [link1, link2, link3]

def correct_cap(title):
    """returns properly capitalized key, blank otherwise"""
    try:
        fl = fln[title]
        return title
    except:
    #capitalize first letter only
        try:
            fl = fln[title[0].upper() + title[1:]]
            return title[0].upper() + title[1:]
        except:
    #try title case
            try:
                fl = fln[title.title()]
                return title.title()
            except KeyError:
                return ""

def traverse_loops(fln, start):
    """
    if true loop,
    returns list of links traversed
    """
    #stop when link is repeated or dead link
    links_traversed = []
    try:
        fl = correct_cap(fln[start])
    except KeyError:
        return False
    i = 0
    while fl not in links_traversed and fl !="":
        #maybe add clicks here?
        i += 1
        #break if too large
        if i > 10000: 
            fl = "exceeded 10k click limit"
            break
        #append fl
        links_traversed.append(fl)
        #jump to next link
        fl = correct_cap(fln[fl])
    if fl in links_traversed:
        return links_traversed
    else:
        return False

def run_traverse(fln, fln_chunk):       
    """
    loops through pages in fln_chunk and 
    1. store true loops in dict 
        - length of loop is key
    """
    nloops_dict = {}
    #key is length -> list of loops (stored as sets)
    i = 0
    for page in fln_chunk.iterkeys():
        i +=1
        if i % 10000 == 0: 
            print i
            gc.collect()
        #traverse path
        page_path = traverse_loops(fln, page)
        if page_path:
            length = len(page_path)
            nloops_dict[page] = length
    return nloops_dict

def write_result(dict, out_path):
    """writes paths to json file"""
    with open(out_path, 'w') as f:
        json.dump(dict, f)

            
if __name__ == "__main__":
    net_path = "/users/m/s/msibrahi/v4/results/flnetwork/"
    #net_path = "/Users/mark/Desktop/wiki_v4/"

    file_num = int(sys.argv[1])

    #load fln dictionary
    with open(net_path + "fln.json") as f:
        fln = json.load(f)

    #load nth fln dictionary
    with open(net_path + str(file_num) + ".json") as f:
        fln_chunk = json.load(f)

    #out_path
    out_path = "/users/m/s/msibrahi/v4/results/paths/" + str(file_num) + "path.json"
    out_path_nloops = "/users/m/s/msibrahi/v4/results/nloops/" + str(file_num) + "nloops.json"
    #out_path = "/Users/mark/Desktop/"+str(file_num) + "path.json"
    #run
    nloops_dict = run_traverse(fln, fln_chunk)
    #write
    #paths
    write_result(nloops_dict, out_path_nloops)

