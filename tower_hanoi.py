def tower(S,I,T,n):
    if n>=1:
        
        tower(S,T,I,n-1)
        print("move disk",n,"from",S,"to",T)

        tower(I,S,T,n-1)

tower("S","I","T",8)