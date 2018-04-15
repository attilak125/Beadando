def kereses(a,b):
    maxegyezes=0
    if(len(a)>len(b)):
        min=len(b)
        max=len(a)
        for i in range(0, max):
            for j in range(0, min):
                if (a[i] == b[j]):
                    count = 0
                    if(max-i>=min-j):
                        aindex = i
                        for bindex in range(j,min):
                            if(a[aindex]==b[bindex]):
                                count+=1
                            elif(count>maxegyezes):
                                maxegyezes=count
                                break
                            else:
                                break
                            aindex += 1
                        if(maxegyezes<count):
                            maxegyezes=count
                    else:
                        bindex = j
                        for aindex in range(i,max):
                            if (a[aindex] == b[bindex]):
                                count += 1
                            elif (count > maxegyezes):
                                maxegyezes = count
                                break
                            else:
                                break
                            bindex += 1
                        if (maxegyezes < count):
                            maxegyezes = count

    else:
        min=len(a)
        max=len(b)
        for i in range(0, max):
            for j in range(0, min):
                if (a[j] == b[i]):
                    count = 0
                    if(max-i>=min-j):
                        bindex = i
                        for aindex in range(j,min):
                            if(a[aindex]==b[bindex]):
                                count+=1
                            elif(count>maxegyezes):
                                maxegyezes=count
                                break
                            else:
                                break
                            bindex += 1
                        if(maxegyezes<count):
                            maxegyezes=count
                    else:
                        aindex = j
                        for bindex in range(i,max):
                            if (a[aindex] == b[bindex]):
                                count += 1
                            elif (count > maxegyezes):
                                maxegyezes = count
                                break
                            else:
                                break
                            aindex += 1
                        if (maxegyezes < count):
                            maxegyezes = count
    print(maxegyezes)
    return 0
kereses("csirke","csirke")