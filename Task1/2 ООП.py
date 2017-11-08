def print_noise(noise):
    print(noise)

class Little_child:
    noise=print_noise
    def __init__(self,n):
        n=2


Petya=Little_child
Petya.noise(4)
