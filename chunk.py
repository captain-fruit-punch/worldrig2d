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

    def update(self, dt): # updates the chunk in which a particle is in
        for i in xrange(0, len(self.particles)):
            cp = self.particles[i] # cp for current particle
            if (

    def clear():
        self.particles = []
