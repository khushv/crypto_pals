
"""
MT19937 Mersenne Twister RNG
constant definitions:

w = word size # number of bits. 32
n = degree of recurrence # 624
m = middle word # 312
r = separation point of one word, or number of bits of the lower bitmask # 31
a = coefficients of the rational normal form twist matrix

w = 32
n = 624
m = 312
r = 31

"""
def rshift(val, n):
    return val>>n if val >= 0 else (val+0x100000000)>>n


class Mersenne_twister:
    def __init__(self, n=624, seed=5489):
        self.seed = seed
        self.state = [0] * n
        self.counter = 624
        self.initialise()

    def int_32(self, number):
        return int(0xFFFFFFFF & number)


    def initialise(self):
        self.state[0] = self.seed
        for i in range(1, len(self.state)):
            #print("state: ", i)
            temp = ((self.state[i-1] ^ (self.state[i-1]) >> 30) ) + i
            self.state[i] = self.int_32(temp * 1812433253)

    def twist(self):
        for i in range(0, 624):
            x = self.state[i] & 0x80000000
            y = self.state[(i+1) % 624] & 0x7fffffff
            z = self.int_32(x + y)

            #next = rshift(z, 1)
            self.state[i] = self.state[(i+397) % 624] ^ (z >> 1)
            if (z %2) == 1:
                self.state[i] ^= 0x9908b0df
            self.counter = 0
            """
            next = z >> 1
            next ^= self.state[(i+397) % 624]
            if (z % 2 ) == 1:
                next ^= 0x9908b0df
            self.state[i] = next
            self.counter = 0
            """


    def generate(self):
        if self.counter >= len(self.state):
            print("twsiting")
            self.twist()

        y = self.state[self.counter]
        #y ^= rshift(y, 11)
        y = y ^ (y>> 11)
        y = y ^ ((y << 7) & 0x9d2c5680)
        y = y ^ ((y << 15) & 0xefc60000)
        #y ^= rshift(y, 18)
        y ^= y >> 18
        self.counter += 1
        return self.int_32(y)

if __name__ == '__main__':
    x = Mersenne_twister()
    print(x.generate())
    print(x.generate())
    #import pdb; pdb.set_trace()
