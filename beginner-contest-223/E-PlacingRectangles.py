x,y,a,b,c = map(int,input().split(' '))

def func2(X,Y,S,T):
    for i in range(2):
        l = S // X + (S % X != 0)
        if l < Y and l * (Y-l) >= T:
            return True
        X,Y = Y,X 
    return False


def func3(X,Y,S,T,R):
    for i in range(2):
        for j in range(3):
            l =  S // X + (S % X != 0)
            if l < Y and func2(X,Y-l,T,R):
                return True

            S,T = T,S  
            T,R = R,T 
        X,Y = Y,X 
    return False 

if func3(x,y,a,b,c):
    print('Yes') 
else:
    print('No')