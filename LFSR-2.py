def draw(S):
    print(S,end=" ")


def LFSR(S):
    while True:
        draw(S)
        newBit = (S ^ (S >> 1) ^ (S >> 2) ^ (S >> 3) ^ (S >> 4)) & 1
        S = (S >> 1) | (newBit << 7)

def main():
    S = (1 << 127) | 1
    LFSR(S)

main()