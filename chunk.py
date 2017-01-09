import particle

class Chunk:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.particles = []

    def createparticles(self, number):
        for particle in xrange(0, number, maxspeed, intensity, maxheat):
            x = random.randrange(w)
            y = random.randrange(h)
            xv = random.randrange(maxspeed)
            yv = random.randrange(maxspeed)
            heat = random.randrange(maxheat)

            self.particles.append(Particle(x, y, xv, yv, intensity, heat))

    def update(self, dt, allchunks) # updates the chunk in which a particle is in
        for particleid in xrange(0, len(self.particle)):
            self.particles[particleid].update(dt)
            c = self.particles[particleid]
            if (c.x > self.w):
                if (c.y > self.h):
                    

    def clear():
        self.particles = []
