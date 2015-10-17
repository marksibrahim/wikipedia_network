"""create a dictionary of links traversed for nth fl chuck"""
#takes a file num and creates xpath.json

import json, gc, sys


#goal path[page] = [link1, link2, link3]

#load fln dictionary
net_path = "/Users/mark/Desktop/wiki_v4/"

with open(net_path + "fln.json") as f:
    fln = json.load(f)
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

def traverse(start):
    """returns list of links traversed"""
    #stop when link is repeated or dead link
    links_traversed = []
    try:
        fl = correct_cap(fln[start])
    except KeyError:
        return "broken link" 
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
    return links_traversed

            
