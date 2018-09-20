width = eval(input('Enter height: '))
height = eval(input('Enter width: '))
for i in range (width*height):
    print(i%10, end=' ')
    if(i>1 and (i+1)%height==0):
        print('')