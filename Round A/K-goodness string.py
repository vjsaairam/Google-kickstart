for case in range(int(input())):
    N,K = map(int,input().split())
    S = input()
    x=0
    for j in range(0,int(len(S)/2)):
        if(S[j]!=S[len(S)-j-1]):
            x+=1
    if (x==K):
        print(f"case #{case+1}: 0")
    elif(x>K):
        
        print(f"case #{case+1}:",x-K)
    else:
        
        print(f"case #{case+1}:",K-x)
