#Armstrong Number-Everything you need to know by DV
while True:
    print(('*')*5,'I N D E X', ('*')*5)
    print('Enter "1" for finding if an number is armstrong or not\nEnter "2" to find armstrong numbers in a specified range\nEnter "3" to Exit')
    q=('D D D     V       V\nD     D    V     V\nD      D    V   V\nD     D      V V\nD D D         V')
    w=int(input('Enter Your Choice: '))
    if w==1:
        a=int(input('Enter The Specific Number: '))
        l=[]
        c=a
        z=0
        while c!=0:
            d=c%10
            l.append(d)
            c=c//10
        for x in range (0,len(l)):
            z=z+(l[x]**len(l))
        if z==a:
            print(a,'is an armstrong number')
        else:
            print(a,'is not an armstrong number')
    elif w==2:
        a=int(input('Enter The Range: '))
        ll=[]
        for g in range(1,a+1):
            i=g
            l=[]
            while i!=0:
                f=i%10
                l.append(f)
                i=i//10
            z=0
            for x in range(0,len(l)):
                z=z+(l[x]**len(l))
            if z==g:
                ll.append(z)
        print('The armstrong numbers between 0 and',a,'are',ll)
    elif w==3 :
        print(q)
        break
    else:
        print('I N V A L I D  C H O I C E')
        print('PRESS ANY KEY TO CONTINUE')
        WEE=input()