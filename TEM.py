n = int(input('Enter the number of rows: '))
s = input('Enter print symbol: ')
j = 1
k = (n*2)-1
for i in range(1,n+1):
    print ((' '*((j-1) ))+(s*k)+(' '*(j-1)))
    j+=1
    k-=2  
     
    

