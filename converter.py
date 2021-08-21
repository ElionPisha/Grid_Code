import h5py
import json
mode = 'r'
path = 'gridcode/AMMICAL-DV.h5'

def generate_json(group):
    result = {}
    for groupKey in group.keys():
        result[groupKey] = generate_json_again(group.get(groupKey))
    return result


def generate_json_again(group):
    result = {}
    for attr in group.attrs.keys():
        result[attr] = group.attrs.get(attr)
    return result


with h5py.File(path, mode) as hdf:
    result = {}
    for key in hdf.keys():
        groupObject = hdf.get(key)
        group = dict(groupObject.items())
        result[key] = generate_json(group)
    print(json.dumps(str(result), indent=10, sort_keys=True))
    hdf.close()