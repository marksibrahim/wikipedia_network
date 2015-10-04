import json

fln_path = "/users/m/s/msibrahi/v4/results/flnetwork/"

fln = {}
for i in range(0, 112):
    with open(fln_path+str(i)+".json") as f:
        fl = json.load(f)
        fln.update(fl)

#write fln.json 

with open(fln_path+"fln.json", "w") as f:
    json.dump(fln, f)

