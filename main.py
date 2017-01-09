import random
import time

import chunk
import graphics
import particle
import world

random.seed(os.urandom)

# get world info
print("def world (in chunks)")

# defaults
worldW = 4
worldH = 4
#worldW = int(raw_input("world width:"))
#worldH = int(raw_input("world height:"))

world1 = world.World(worldW, worldH)

tc = time.clock() # last time
tl = 0 # time it took to execute last frame

while True:
    # perform analysis (calculating delta time)
    tl = time.clock() - tc # find dt
