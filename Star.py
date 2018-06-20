n = int(input('Enter a number'))
i=1;j=1
while 1:
    try:
        for i in range(n+1):
            print i*'*'
        break
    except:
        print 'Error'
    

