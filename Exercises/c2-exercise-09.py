num = eval(input('Enter the number: '))
first_num = 1
second_num = 1
for i in range(num):
    print(first_num)
    temp = second_num
    second_num = second_num + first_num
    first_num = temp
