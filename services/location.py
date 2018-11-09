class Location:
    __slots__ = ['x', 'y']
    def __init__(x, y):
        pass

class World:
    # Grid
    REGIONS_WH = (100.0, 100.0)
    NG = (10,10)

REGIONS_WH0 = World.REGIONS_WH[0]
REGIONS_WH1 = World.REGIONS_WH[1]
NCOLS = World.NG[0]
NROWS = World.NG[1]
N2 = NCOLS * NROWS

#Region = int  ---> in fact a tuple of 2

def region(loc -> Location):
    rx = int(loc.x / REGIONS_WH0)
    ry = int(loc.y / REGIONS_WH1)
    return (rx, ry)

def region_hash(loc -> Location):
    rxy = region(loc)
    w = rxy[0] % NCOLS
    h = rxy[1] % NROWS
    i =  w + NCOLS*h
    assert i < N2
    return i

#def region_server(reg):

def region_server_no(loc -> Location):
    r01 = region(loc)
    return (r01[0] + r01[1]) % 2
