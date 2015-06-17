class Editdistance(object):

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
    def ED(s,t,match,mismatch,gap):
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
                d[i,j]=min(d[i-1,j-1] + MATCH(s[i-1],t[j-1],match,mismatch),d[i-1,j] + GAP(1,0,1),d[i,j-1] + GAP(1,0,1))

	#Print 함수 추가
        PRINTF (n,m,d)
        print "edit distance =", d[n,m]
    

