import chunk
import graphics
import particle
import world

print("def world (in chunks)")
worldW = int(raw_input("world width:"))
worldH = int(raw_input("world height:"))

world1 = world.World(worldW, worldH)
