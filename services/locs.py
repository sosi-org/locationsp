from location import N2
from location import Location
from location import region_hash


#dbr = [{}, {}]
#dbr = [[], []]
dbr = list(map(lambda x: list(), range(N2)))

def dbarray(loc: Location):
    #rxy = region(loc)
    #dbr[rxy[0]][rxy[1]].append(loc)
    i = region_hash(loc)
    return dbr[i]



import numpy as np

def all_locs_numpy(hash):
    a = np.toarray(dbr[hash])
    return a

# never use
def all_locs_numpy_total(hash):
    for hash in range(len(dbr)):
        a = np.toarray(dbr[hash])
        raise NotImplemented()
