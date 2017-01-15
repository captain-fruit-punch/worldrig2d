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

world1init = {'wordW':4, 'worldH':4}

#world1init['worldW'] = int(raw_input("world width:"))
#world1init['worldH'] = int(raw_input("world height:"))

world1 = world.World(world1init['worldW'], world1init['worldH'])

tc = time.clock() # last time
tl = 0 # time it took to execute last frame

while True:
    # perform analysis (calculating delta time)
    tl = time.clock() - tc # find dt
