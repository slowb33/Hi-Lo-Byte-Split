#!/usr/local/bin/python3
# Extremely basic high/low byte splitter for ROMS -- Public Domain

import os

fin = open( "tos.img", "rb" )

infilesize = os.stat("tos.img").st_size

fhi = open( "2way_high.img", "wb" )
flo = open( "2way_low.img", "wb" )

byte = 1                # just want the next test to pass
while byte:             # stop at EOF
    byte = fin.read(1)  # read one byte
    fhi.write(byte)     # write it to the high file

    byte = fin.read(1)  # read one more byte
    flo.write(byte)     # write it the low file, then repeat

fin.close()
fhi.close()
flo.close()

# let's then further split those into 6 for the pre-STE range

fhi = open( "2way_high.img", "rb" )
flo = open( "2way_low.img", "rb" )

fhi0 = open( "6way_high_0.img", "wb" )
fhi1 = open( "6way_high_1.img", "wb" )
fhi2 = open( "6way_high_2.img", "wb" )

flo0 = open( "6way_low_0.img", "wb" )
flo1 = open( "6way_low_1.img", "wb" )
flo2 = open( "6way_low_2.img", "wb" )

byte = 1                 # just want the next test to pass
while byte:              # stop at EOF
    data = fhi.read(1)   # read one byte 
    fhi0.write(data)     # write it to the high 0 file

    data = fhi.read(1)   # read one another byte
    fhi1.write(data)     # write it to the high 1 file

    data = fhi.read(1)   # read one further byte
    fhi2.write(data)     # write it to the high 2 file

    # same now for low

    data = flo.read(1)   # read one byte
    flo0.write(data)     # write it to the low 0 file

    data = flo.read(1)   # read one another byte
    flo1.write(data)     # write it to the low 1 file

    data = flo.read(1)   # read one further byte
    flo2.write(data)     # write it to the low 2 file


fhi.close()
flo.close()

fhi0.close()
fhi1.close()
fhi2.close()

flo0.close()
flo1.close()
flo2.close()
