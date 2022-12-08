#!/usr/bin/env -S conda run -n py2 python

import sys,os
import pandas as pd


# Set this value to the location of Pizza Py Tools
path = os.environ["LAMMPS_PYTHON_TOOLS"]
sys.path.append(path)
from data import data


dat = data(sys.argv[1]+".data")
box=dat.headers["xlo xhi"]
box_z=dat.headers["zlo zhi"]
box_mod = list(box)
dat.headers["zlo zhi"]=tuple(box_mod)
dat.headers["xlo xhi"]=box_z
x_coords = dat.get("Atoms",5)
dat.replace("Atoms",5,x_coords)
dat.reorder("Atoms",1,2,3,4,7,6,5)

dat.write(sys.argv[1]+"_edit.data")

if len(sys.argv) == 3:
    reorder_dict = eval(sys.argv[2])
    types = dat.get("Atoms",3)
    types_modified = [reorder_dict[int(type)] for type in types]
    dat.replace("Atoms",3,types_modified)
    
