import os
#print("yeah")
#set environment variable
#os.environ["GAIA_TOOLS_DATA"] = "/home/ferrer/gilaa/GAIATOOLSDATA"
#print(os.getenv("GAIA_TOOLS_DATA"))
import gaia_tools.load as gload
import apogee
from astropy.io import fits

apogee_cat = gload.apogee()
print(type(apogee_cat))
