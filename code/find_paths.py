"""create a dictionary of links traversed for nth fl chuck"""
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

def traverse(fln, start):
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

def return_feeder_page(fln, page, page_path):
    """returns feeder page if any"""
    if len(page_path) > 1:
        fl = correct_cap(fln[page_path[-1]])
        if fl in page_path and fl != "":
            return fl
    return ""


def run_traverse(fln, fln_chunk):       
    """loops through pages in fln_chunk and 
    1. stores paths traversed
    2. stores clicks
    3. stores len of path
    4. stores clicks of page feeding into loop """
    paths_chunk = {}
    clicks_chunk = {} #page: clicks
    path_length_chunk = {}  #page : path length
    feed_count_chunk = {} #page : feed clicks
    i = 0
    for page in fln_chunk.iterkeys():
        i +=1
        if i % 10000 == 0: 
            print i
            gc.collect()
        #traverse path
        page_path = traverse(fln, page)
        #add to dictionary
        paths_chunk[page] = page_path
        #update clicks 
        for pt in page_path:
            clicks_chunk[pt] = clicks_chunk.get(pt, 0) + 1
        #update len(path) 
        path_length_chunk[page] = len(page_path)
        #update feeder clicks
        feeder = return_feeder_page(fln, page, page_path)
        if feeder:
            feed_count_chunk[feeder] = feed_count_chunk.get(feeder, 0) + 1
    return paths_chunk, clicks_chunk, path_length_chunk, feed_count_chunk

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
    out_click =  "/users/m/s/msibrahi/v4/results/clicks/" + str(file_num) + "click.json"
    out_length =  "/users/m/s/msibrahi/v4/results/path_length/" + str(file_num) + "length.json"
    out_feed_count =  "/users/m/s/msibrahi/v4/results/feed_count/" + str(file_num) + "feed_count.json"
    #out_path = "/Users/mark/Desktop/"+str(file_num) + "path.json"
    #run
    paths_chunk, clicks_chunk, path_length_chunk, feed_count_chunk = run_traverse(fln, fln_chunk)
    #write
    #paths
    write_result(paths_chunk, out_path)
    write_result(clicks_chunk, out_click)
    write_result(path_length_chunk, out_length)
    write_result(feed_count_chunk, out_feed_count)
    


