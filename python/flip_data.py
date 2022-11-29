#!/usr/bin/env -S conda run -n py2 python

import sys,os
import pandas as pd
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
#x_mod = [x+5 for x in x_coords]
dat.replace("Atoms",5,x_coords)
dat.reorder("Atoms",1,2,3,4,7,6,5)
dat.write(sys.argv[1]+"_edit.data")

#dat.write("nafion.data")

