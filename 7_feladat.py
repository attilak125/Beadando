
def palindromic(a):
    b=a.lower()
    normalstring=''
    reverstring=''
    for i in b:
        if 'a' <= i <= 'z':
            normalstring+=i
    for i in range (len(normalstring)-1,-1,-1):
        reverstring+=normalstring[i]

    for i in range(0,len(normalstring)):
        


    # seged=''
    # world=''
    # num=0
    # max=0
    # for ch in b:
    #     if 'a'<= ch <= 'z':
    #         world+=ch
    #     else:
    #         for i in range (len(world)-1,-1,-1):
    #             seged+=world[i]
    #         seged+=ch
    #         world=''
    # for i in range(len(world) - 1, -1, -1):
    #     seged += world[i]
    # seged += ch
    # for i in range(0,len(b)-1):
    #     if(seged[i]==b[i]):
    #         num+=1
    #     elif(num>max):
    #         max=num
    #         num=0
    #     else:
    #         num=0
    # print(max)
    return 0





palindromic("saS feszke mAgasan van lol")