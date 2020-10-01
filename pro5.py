def generateMatrix(self, A):
        n = A
        res = [[0]*n for i in range(n)]
        T = 0
        B = len(res)- 1
        L = 0
        R = len(res[0]) -1
        dir = 0
        cont = 1
        while T <= B and L <= R :
            if dir == 0:
                for i in range(L,R+1):
                    res[T][i] = cont
                    cont +=1
                T += 1
            elif dir == 1:
                for i in range(T,B+1):
                    res[i][R] = cont
                    cont +=1
                R -= 1
            elif dir == 2:
                for i in range(R,L-1,-1):
                    res[B][i] = cont
                    cont +=1
                B -= 1
            else:
                #dir == 3:
                for i in range(B,T-1,-1):
                    res[i][L] = cont
                    cont +=1
                L += 1
            dir = (dir+1)%4
        return res
