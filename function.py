class Edit_dis:
        

#Edit distance table
    def PRINTF(self,n,m,d):
        for i in range(n+1):
            row=[]
            for j in range(m+1):
                row.append(d[i,j])
            print row
#Match
    def MATCH11(self,a,b,match,mismatch):
        if (a==b):
            return match
        else:
            return mismatch

#Gap penalty(v:open, u:gap, i:gap length)
    def GAP(self,i,u,v):
        return u*i+v
    
    

    
    



