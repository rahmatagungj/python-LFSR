def draw(S):
    print(S,end=" ")


def LFSR(S,n):
    for i in range(n):
        S = S[1:] + S[0]
        draw(S)

def main():
    S = "01010101"
    n = 1000
    LFSR(S,n)

main()