
import json

fldict = {}
for i in range(112):
    fpath = "/users/m/s/msibrahi/v3/results/flnetwork/" + str(i) + ".json"
    with open(fpath, 'r') as f:
        data = json.load(f)
        fldict.update(data)

out_path = "/users/m/s/msibrahi/v3/results/flnetwork/fldict.json"
with open(out_path, 'w') as outfile:
    json.dump(fldict, outfile)
