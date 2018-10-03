width = eval(input('Enter width: '))
height = eval(input('Enter height: '))
for i in range (width*height):
    print(i%10, end=' ')
    if(i>1 and (i+1)%width==0):
        print('')