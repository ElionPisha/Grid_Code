import h5py
import json

mode = 'r'
path = 'gridcode/AMMICAL-DV.h5'

def visitor_func(name, node):
    if isinstance(node, h5py.Dataset):
        print(name + " : ", node)

with h5py.File(path, mode) as hdf:
      hdf.visititems(visitor_func)
      hdf.close()



json_string = """{
{'Kraft': <HDF5 dataset "Kraft": shape (15987,), type "<f4">, 'KraftWegM': <HDF5 dataset "KraftWegM": shape (16000,), type "<f4">, 'KraftWegWi': <HDF5 dataset "KraftWegWi": shape (16000,), type "<f4">, 'Spa': <HDF5 dataset "Spa": shape (15987,), type "<f4">, 'SpaStaWi': <HDF5 dataset "SpaStaWi": shape (16000,), type "<f4">, 'StaWi': <HDF5 dataset "StaWi": shape (15987,), type "<f4">, 'WegM': <HDF5 dataset "WegM": shape (15987,), type "<f4">, 'WegWi': <HDF5 dataset "WegWi": shape (15987,), type "<f4">}
{'Kraft': <HDF5 dataset "Kraft": shape (15604,), type "<f4">, 'KraftWegM': <HDF5 dataset "KraftWegM": shape (16000,), type "<f4">, 'KraftWegWi': <HDF5 dataset "KraftWegWi": shape (16000,), type "<f4">, 'Spa': <HDF5 dataset "Spa": shape (15604,), type "<f4">, 'SpaStaWi': <HDF5 dataset "SpaStaWi": shape (16000,), type "<f4">, 'StaWi': <HDF5 dataset "StaWi": shape (15604,), type "<f4">, 'WegM': <HDF5 dataset "WegM": shape (15604,), type "<f4">, 'WegWi': <HDF5 dataset "WegWi": shape (15604,), type "<f4">}
{'Kraft': <HDF5 dataset "Kraft": shape (15466,), type "<f4">, 'KraftWegM': <HDF5 dataset "KraftWegM": shape (16000,), type "<f4">, 'KraftWegWi': <HDF5 dataset "KraftWegWi": shape (16000,), type "<f4">, 'Spa': <HDF5 dataset "Spa": shape (15466,), type "<f4">, 'SpaStaWi': <HDF5 dataset "SpaStaWi": shape (16000,), type "<f4">, 'StaWi': <HDF5 dataset "StaWi": shape (15466,), type "<f4">, 'WegM': <HDF5 dataset "WegM": shape (15466,), type "<f4">, 'WegWi': <HDF5 dataset "WegWi": shape (15466,), type "<f4">}
{'Kraft': <HDF5 dataset "Kraft": shape (15982,), type "<f4">, 'KraftWegM': <HDF5 dataset "KraftWegM": shape (16000,), type "<f4">, 'KraftWegWi': <HDF5 dataset "KraftWegWi": shape (16000,), type "<f4">, 'Spa': <HDF5 dataset "Spa": shape (15982,), type "<f4">, 'SpaStaWi': <HDF5 dataset "SpaStaWi": shape (16000,), type "<f4">, 'StaWi': <HDF5 dataset "StaWi": shape (15982,), type "<f4">, 'WegM': <HDF5 dataset "WegM": shape (15982,), type "<f4">, 'WegWi': <HDF5 dataset "WegWi": shape (15982,), type "<f4">}
{'Kraft': <HDF5 dataset "Kraft": shape (15985,), type "<f4">, 'KraftWegM': <HDF5 dataset "KraftWegM": shape (16000,), type "<f4">, 'KraftWegWi': <HDF5 dataset "KraftWegWi": shape (16000,), type "<f4">, 'Spa': <HDF5 dataset "Spa": shape (15985,), type "<f4">, 'SpaStaWi': <HDF5 dataset "SpaStaWi": shape (16000,), type "<f4">, 'StaWi': <HDF5 dataset "StaWi": shape (15985,), type "<f4">, 'WegM': <HDF5 dataset "WegM": shape (15985,), type "<f4">, 'WegWi': <HDF5 dataset "WegWi": shape (15985,), type "<f4">}
{'Kraft': <HDF5 dataset "Kraft": shape (15986,), type "<f4">, 'KraftWegM': <HDF5 dataset "KraftWegM": shape (16000,), type "<f4">, 'KraftWegWi': <HDF5 dataset "KraftWegWi": shape (16000,), type "<f4">, 'Spa': <HDF5 dataset "Spa": shape (15986,), type "<f4">, 'SpaStaWi': <HDF5 dataset "SpaStaWi": shape (16000,), type "<f4">, 'StaWi': <HDF5 dataset "StaWi": shape (15986,), type "<f4">, 'WegM': <HDF5 dataset "WegM": shape (15986,), type "<f4">, 'WegWi': <HDF5 dataset "WegWi": shape (15986,), type "<f4">}
{'Kraft': <HDF5 dataset "Kraft": shape (15984,), type "<f4">, 'KraftWegM': <HDF5 dataset "KraftWegM": shape (16000,), type "<f4">, 'KraftWegWi': <HDF5 dataset "KraftWegWi": shape (16000,), type "<f4">, 'Spa': <HDF5 dataset "Spa": shape (15984,), type "<f4">, 'SpaStaWi': <HDF5 dataset "SpaStaWi": shape (16000,), type "<f4">, 'StaWi': <HDF5 dataset "StaWi": shape (15984,), type "<f4">, 'WegM': <HDF5 dataset "WegM": shape (15984,), type "<f4">, 'WegWi': <HDF5 dataset "WegWi": shape (15984,), type "<f4">}
}"""

to_json = json.dumps(json_string)
print("JSON Output ", to_json)