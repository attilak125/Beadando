
def palindromic(a):
    b=a.lower()
    seged=''
    world=''
    for ch in b:
        if 'a'<= ch <= 'z':
            world+=ch
        else:
            for i in range (len(world)-1,-1,-1):
                seged+=world[i]
            seged+=ch
            world=''
            
    return 0





palindromic("saS feszke mAgasan van lol")