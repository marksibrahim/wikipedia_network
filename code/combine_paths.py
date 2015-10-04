
import json, gc, sys

paths_path = "/users/m/s/msibrahi/v4/results/paths/"

paths = {}
s = int(sys.argv[1])
n = int(sys.argv[2])

for i in range(s, n):
    with open(paths_path+str(i)+"path.json") as f:
        path_chunk = json.load(f)
        paths.update(path_chunk)

#write fln.json 

with open(paths_path + "cpaths" + str(s) + "_" + str(n) + ".json", "w") as f:
    json.dump(paths, f)

