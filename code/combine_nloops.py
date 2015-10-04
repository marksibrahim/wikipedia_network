
import json, gc

length_path = "/users/m/s/msibrahi/v4/results/nloops/"

nloops = {}

#list of files 
files = [str(i)+"nloops.json" for i in range(112)]
 
for file in files:
    with open(length_path + file) as f:
        nloop = json.load(f)
    nloops.update(nloop)


with open(length_path + "nloops.json", "w") as f:
    json.dump(nloops, f)

