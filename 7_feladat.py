
def palindromic(a):
    b=a.lower()
    normalstring=''
    reverstring=''
    egyezes=''
    maxegyezes=''
    szamlalo=0
    maximum=0
    for i in b:
        if 'a' <= i <= 'z':
            normalstring+=i
    for i in range (len(normalstring)-1,-1,-1):
        reverstring+=normalstring[i]

    for i in range(0,len(normalstring)):
        if normalstring[i] == reverstring[i]:
            egyezes+=reverstring[i]
            szamlalo+=1
        elif szamlalo > maximum:
            maxegyezes=egyezes
            maximum=szamlalo
            egyezes=''
            szamlalo=0
        else:
            egyezes=''
            szamlalo=0
    if szamlalo > maximum:
        maxegyezes=egyezes
        maximum=szamlalo
    print(maxegyezes)
    print(maximum)


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





palindromic("a gorog a")