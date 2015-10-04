import json, gc

clicks_path = "/users/m/s/msibrahi/v4/results/feed_count/"
fln_path = "/users/m/s/msibrahi/v4/results/flnetwork/fln.json"

#load list of pages
with open(fln_path) as f:
    fln = json.load(f)

clicks = {}

clicks_files = []

#add clicks_files to list
for i in range(0, 112):
    with open(clicks_path +str(i)+"feed_count.json") as f:
        clicks_chunk = json.load(f)
        clicks_files.append(clicks_chunk)

p = 0 
for page in fln.iterkeys():
    p += 1
    if p % 10000 == 0: gc.collect()
    page_clicks = 0 
    for i in range(0, 112):
        if page in clicks_files[i]:
            page_clicks += clicks_files[i][page]
    clicks[page] = page_clicks
        


with open(clicks_path + "feed_count.json", "w") as f:
    json.dump(clicks, f)
