def kreses(a,b):
    maxegyezes=0
    if(len(a)>len(b))
        min=len(b)-1
        max=len(a)-1
    for i in range(0,max):
        for j in range(0,min):
            if(a[i]==b[j]):
                count=0
                aindex = i
                bindex = j
                while(1):
                    if(aindex<max|bindex<min):
                        if(a[aindex]==b[bindex]):
                            count+=1
                        elif(maxegyezes<count):
                            maxegyezes=count
                            count=0
                            break
                        else:
                            count=0
                            break
                    aindex+=1
                    bindex+=1