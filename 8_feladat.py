def kereses(a,b):
    maxegyezes=0
    if(len(a)>len(b)):
        min=len(b)
        max=len(a)
        for i in range(0, max):
            for j in range(0, min):
                if (a[i] == b[j]):
                    count = 0
                    if(max-i>min-j):
                        aindex = i
                        for bindex in range(j,min):
                            if(a[aindex]==b[bindex]):
                                count+=1
                                print(count,maxegyezes)
                            elif(count>maxegyezes):
                                maxegyezes=count
                                break
                            else:
                                break
                            aindex += 1
                        if(maxegyezes<count):
                            maxegyezes=count

    # else:
    #     max=len(b)
    #     min=len(a)
    #     for i in range(0,max):
    #         for j in range(0,min):
    #             if(a[j]==b[i]):
    #                 count=0
    #                 aindex = j
    #                 bindex = i
    #                 while(1):
    #                     if(aindex<=max|bindex<=min):
    #                         if(a[aindex]==b[bindex]):
    #                             count+=1
    #                         elif(maxegyezes<count):
    #                             maxegyezes=count
    #                             count=0
    #                             break
    #                         else:
    #                             count=0
    #                             break
    #                     aindex+=1
    #                     bindex+=1
    print(maxegyezes)
    return 0
kereses("Az egy csirke a placon","csirke")