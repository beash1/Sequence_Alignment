s=raw_input("Enter first sequence :")
t=raw_input("Enter second sequence :")
u=int(raw_input("Enter gap penalty :"))
v=0
match = int(raw_input("Enter match score :"))
mismatch = int(raw_input("Enter mismatch score :"))


    #Edit distance table
def PRINTF(n,m,d):
    for i in range(n+1):
        row=[]
        for j in range(m+1):
            row.append(d[i,j])
        print row
       
    #두 서열에서 각 nuclotide가 같은지 확인
def MATCH(a,b,match,mismatch):
    if (a==b):
        return match
    else:
        return mismatch

    #gap penalty(v:open, u:gap, i:gap length)
def GAP(i,u,v):
    return u*i+v

    #Editdistance 계산
def ED(s,t,match,mismatch,u,v):
    n = len(s)
    m = len(t)
    d = {}
    for i in range(n+1):
        for j in range(m+1):
            d[i,j]=0
    
    for i in range(n+1):
        d[i,0]= i
    for j in range(m+1):
        d[0,j]= j
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            d[i,j]=min(d[i-1,j-1] + MATCH(s[i-1],t[j-1],match,mismatch),d[i-1,j] + GAP(1,u,v),d[i,j-1] + GAP(1,u,v))

    #Print 함수 추가
    PRINTF (n,m,d)
    print "edit distance =", d[n,m]

    b = {}
    for i in range(n+1):
        for j in range(m+1):
            b[i,j]=0

    for i in range(n+1):
        b[i,0]= 2
    for j in range(m+1):
        b[0,j]= 4
    

    for i in range(1,n+1):
        for j in range(1,m+1):
            if (d[i,j]==(d[i-1,j-1] + MATCH(s[i-1],t[j-1],match,mismatch))):
                b[i,j]= b[i,j]+1;
            if (d[i,j]==(d[i-1,j] + GAP(1,0,1))):
                b[i,j]= b[i,j]+2;
            if (d[i,j]==(d[i,j-1] + GAP(1,0,1))):
                b[i,j]= b[i,j]+4;
    
    PRINTF(n,m,b)

    x=''
    y=''
    BACK(n,m,b,s,t,x,y)

def BACK(i,j,b,s,t,x,y):
    
    if ((i==0) and (j==0)):
        print x
        print y
        print "\n"
    else:
        if ( b[i,j] & 1 ) == 1 :
            BACK(i-1,j-1,b,s,t,s[i-1]+x,t[j-1]+y)
        if ( b[i,j] & 2 ) == 2 :
            BACK(i-1,j,b,s,t,s[i-1]+x,"-"+y)
        if ( b[i,j] & 4 ) == 4 :
            BACK(i,j-1,b,s,t,"-"+x,t[j-1]+y)


ED(s,t,match,mismatch,u,v)

