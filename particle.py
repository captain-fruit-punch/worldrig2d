# currentchunk = {} (commented out because paricles interact beyond their chunk)holds particles in current chunk
# check chunks surrounding single chunk of which the particle exists

#each chunk is characterized by the max interaction distance of the particles
#world size is characterized by number of chunks, and therefore the chunk's size

curpartchunk = [] #current particles in chunk

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.currentchunk

    def reduce():
        store = x/(x+y)
        y = y/(x+y)
        x = store

class Particle:
    def __init__(self, x, y, vx, vy, intensity, heat):
        self.x  = x  # x position within chunk
        self.y  = y  # y position within chunk
        self.vx = vx # x vector
        self.vy = vy # y vector
        self.intensity = intensity # interaction intensity (also seen as mass, and therefore size)
        self.heat = heat # heat of particle i.e. random movement
        self.chunkx = 0
        self.chunky = 0

    def distance(self, particle2): # returns the distance between two particles
        vecx = abs(self.x - particle2.x)
        vecy = abs(self.y - particle2.y)
        return sqrt((vecX ** 2) + (vecY ** 2))

    def repulsion(self, particle2): # returns a vector of the degree of force to be applied to both particles
        vecx = abs(self.intensity * (self.x - particle2.x))
        vecy = abs(self.intensity * (self.y - particle2.y))

        if (particle2.x > self.x):
            curpartchunk[particle2.id].vx = curpartchunk[particle2.id].vx + vecx
        else:
            curpartchunk[particle2.id].vx = curpartchunk[particle2.id].vx - vecx

        if (particle2.y > self.y)
            curpartchunk[particle2.id].vy = curpartchunk[particle2.id].vy + vecy
        else:
            curpartchunk[particle2.id].vy = curpartchunk[particle2.id].vy - vecy

    def update(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt

    def collide(self, particle2): # returns the new travel vectors of particles
        tempstore = particle2.vx
        particle2.vx = particle2.vy
        particle2.vy = tempstore
        tempstore = self.vx
        self.vy = self.vx
        self.vx = tempstore
