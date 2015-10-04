

import xml.etree.ElementTree as ET
import first_link_txt, gc, json, string, sys


#data_path = "/Volumes/mark external/wikipedia/enwiki_20141106.xml"
#data_path = "/Volumes/mark external/wikipedia/clean_small/smallaf.xml"
data_path = "/Users/mark/Desktop/wiki_v3/smallag.xml"
out_path = "/Users/mark/Desktop/test.json"



def create_tree(data_path):
    """xml tree object for parsing"""
    parser = ET.XMLParser()
    tree = ET.iterparse(data_path)
    return tree

def get_title(elem):
    """return title after checking"""
    #validate title
    if first_link_txt.check_link(elem.text):
        try: 
            title = elem.text
        except:
            title = ""
    else: 
        title = ""
    return title

def get_fl(elem):
    """validate, return first link"""
    try:
        fl = first_link_txt.run_parser(elem.text)
    except:
        fl = ""
    return fl
    
def process_xml(data_path):
    """goes through each page in xml
    returns dictionary: title -> first link"""
    tree = create_tree(data_path)
    
    #initialize vars
    fldict = {}
    p = 0
    title = ""
    fl = ""
    
    for action, elem in tree:
        #free memory
        if p % 100 == 0: gc.collect() 
        
        if elem.tag[-4:] == "page":
            #count
            p += 1
            if p > 1000: break
            
            #write
            if title and fl:
                fldict[title] = fl
            
            #reset
            title = ""
            fl = ""
            
        if elem.tag[-5:] == "title":
            title = get_title(elem)
        
        if elem.tag[-4:] == "text" and title:
            fl = get_fl(elem)
    
    return fldict

def store_json(fldict, out_path):
    """stores fldict as json file"""
    with open(out_path, 'w') as outfile:
        json.dump(fldict, outfile)

def run_process(data_path, out_path):
    """process xml and stores result in json"""
    fldict = process_xml(data_path)
    store_json(fldict, out_path)
    
#to load json
#with open(out_path, 'r') as jdict:
#    fldict = json.load(jdict)


if __name__ == "__main__":
    #can be called with argument for file number 
    #list of 112 files
    letter_range = ["a", "b", "c", "d"]
    file_list = [a + b for a in ["small" + a for a in letter_range] for b in list(string.ascii_lowercase)]
    extra_files = ["small" + a for a in ["ea", "eb", "ec", "ed", "ee", "ef", "eg", "eh"]]

    full_file_list = file_list + extra_files
    
    #variables 
    file_num = int(sys.argv[1])
    data_path = "/users/m/s/msibrahi/full_wiki_data/" + full_file_list[file_num] + ".xml"
    out_path = "/user/ms/s/msibrahi/first_link_network/" + str(file_num) + ".json"
    data_path = "/Users/mark/Desktop/wiki_v3/"  + full_file_list[file_num] + ".xml"
    out_path = "/Users/mark/Desktop/" + str(file_num) + ".json"

    run_process(data_path, out_path)





