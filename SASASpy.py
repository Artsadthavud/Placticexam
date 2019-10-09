print ("Select 2 options")
print (" - 1 encrypt with ROT 13")
print (" - 2 decrypt with ROT 13")
ch = input("\nChoose option: ")
sen = input("Enter text: ")
count = len(sen)
z = ord('1')
zz = ord('9')
zzz = ord('a')
zzzz = ord('z')
zzzzz = ord('A')
zzzzzz = ord('Z')

 # ENclyp
if ch == '1' or ch == '-1':
    print ('Ciphertext is "',end='')
    for i in range (0,count):
       n = ord(sen[i])
       # find num
       if n >= z and n <= zz :
            print(sen[i],end='')
        # find a-z
       elif n >= zzz and n <= zzzz:  
             if n+13 > zzzz :
                print(chr((((n+13) - zzzz)+zzz)-1),end='')
             elif n+13 <= zzzz :
                 print(chr(n+13),end='')
        # find A-Z
       elif n >= zzzzz and n <= zzzzzz :
             if n+13 > zzzzzz :
                 print(chr((((n+13) - zzzzzz)+zzzzz)-1),end='')
             elif n+13 <= zzzzzz :
                 print (chr(n+13),end='')
       else :
            print(sen[i],end='') 

# DEclyp
elif ch == '2'or ch == '-1' : 
    print ('Plaintext is "',end='')
    
    for i in range (0,count) :
        n = ord(sen[i])
           # find num
        if n >= z and n <= zz :
              print(sen[i],end='')

        # find a-z
        elif n >= zzz and n <= zzzz:  
             if n-13 < zzz :
                print(chr((zzzz - ( zzz - (n-13))+1)),end='')
             elif n-13 >= zzz :
                 print(chr(n-13),end='')
        # find A-Z
        elif n >= zzzzz and n <= zzzzzz :
             if n-13 < zzzzz :
                 print(chr((zzzzzz - ( zzzzz - (n-13))+1)),end='')
             elif n-13 >= zzzzz :
                 print (chr(n-13),end='')
        else :
            print(sen[i],end='')
print('"')