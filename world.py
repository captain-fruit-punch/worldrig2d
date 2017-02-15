import chunk


class World:
    def __init__(self, w, h):
        self.chunks = [] # all chunks within world
        self.addp = [] # particles qued to be added to other chunks

        t = [Chunk()] * w
        self.chunks = t * h

        for x in xrange(0, w):
            hwe = [] # hwe for lack of a better name
            for y in xrange(0, h):
                hwe.append(chunk.Chunk(x, y))
            self.chunks.append(hwe)

    def surrounding(self, doself):
        out = []
        global allchunks
        if(doself): #add self to array
            out.append(self)
        # to make it easier, i've organized it in this order:
        #  0 1 2
        #  3 - 4
        #  5 6 7
        # (did not indent the following because the "#" also means "number"
        out.grabbedchunks.append(allchunks[self.x-1][self.y+1]) #0 -1,  1
        out.grabbedchunks.append(allchunks[self.x  ][self.y+1]) #1  0,  1
        out.grabbedchunks.append(allchunks[self.x+1][self.y+1]) #2  1,  1
        out.grabbedchunks.append(allchunks[self.x-1][self.y  ]) #3 -1,  0
        #deleted because of center chunk, but I might have to put it in
        out.grabbedchunks.append(allchunks[self.x+1][self.y  ]) #4  1,  0
        out.grabbedchunks.append(allchunks[self.x-1][self.y-1]) #5 -1, -1
        out.grabbedchunks.append(allchunks[self.x  ][self.y-1]) #6  0. -1
        out.grabbedchunks.append(allchunks[self.x+1][self.y-1]) #7  1, -1

    def moveparticle(self, chunkid1, particleid1, chunkid2, particleid2):

    def moveparticlesfromchunks(self):
        for cc in self.chunks:
            for cp in cc.particles:
                self.chunks[cc.x][cc.y].particles[cp.id]

    def updateparticleids(self):
