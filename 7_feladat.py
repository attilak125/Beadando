
def palindromic(a):
    worlds= a.split(" ")
    print(worlds)
    for world in worlds:
        seged=len(world)-1
        help=False
        for i in range(0,len(world)):
            if(world[i]==world[seged]):
                help=True
            else:
                help=False
                break
            seged-=1
        if help:
            print(world)
    return 0





palindromic("sas fészke magasan van lol")