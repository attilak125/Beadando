
def palindromic(a):
    b=a.lower()
    normalstring=''
    reverstring=''
    egyezes=''
    maxegyezes=''
    szamlalo=0
    maximum=0
    egyezeshelye=0
    for i in b:
        if 'a' <= i <= 'z':
            normalstring+=i
    for i in range (len(normalstring)-1,-1,-1):
        reverstring+=normalstring[i]
    print(reverstring, normalstring)

    for i in range(0,len(normalstring)):
        for j in range(egyezeshelye,len(reverstring)):
            if normalstring[i] == reverstring [j]:
                if i > j:
                    seged = i-j
                    segedindex=0
                    for index in range(i,len(reverstring)):
                        segedindex= index-seged
                        if normalstring[index] == reverstring[segedindex]:
                            egyezes+=normalstring[index]
                            print(egyezes)
                            szamlalo+=1
                        else:
                            break
                else:
                    seged=j-i
                    segedindex=0
                    for index in range(j,len(reverstring)):
                        segedindex=index-seged
                        if normalstring[segedindex] == reverstring[index]:
                            egyezes+=normalstring[segedindex]
                            szamlalo+=1
                        else:
                            break
            if szamlalo > maximum:
                maxegyezes = egyezes
                maximum = szamlalo
                szamlalo = 0
                egyezes = ''
            else:
                szamlalo = 0
                egyezes = ''

    if szamlalo > maximum:
        maxegyezes=egyezes
        maximum=szamlalo
    print(maxegyezes)
    print(maximum)

    return 0





palindromic("banana")