
import json, gc

length_path = "/users/m/s/msibrahi/v4/results/path_length/"
fln_path = "/users/m/s/msibrahi/v4/results/flnetwork/fln.json"

#load list of pages
with open(fln_path) as f:
    fln = json.load(f)

lengths = {}

length_files = []

#add length_files to list
for i in range(0, 112):
    with open(length_path +str(i)+"length.json") as f:
        lengths_chunk = json.load(f)
        length_files.append(lengths_chunk)

p = 0 
for page in fln.iterkeys():
    p += 1
    if p % 10000 == 0: gc.collect()
    page_length = 0 
    for i in range(0, 112):
        if page in length_files[i]:
            page_length += length_files[i][page]
    lengths[page] = page_length
        


with open(length_path + "lengths.json", "w") as f:
    json.dump(lengths, f)

