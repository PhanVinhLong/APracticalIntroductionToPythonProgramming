from random import randint
s = input('Enter a string: ')
s = s.lower()
key = []

result = [ord(c) for c in s]
for i in range(0, len(result)):
    if result[i]>=97 and result[i]<=122:
        key.append(randint(1,26))
        a = key[-1]
        result[i] = result[i]+key[-1]
        if result[i]>122:
            result[i] = result[i]-26
print('encrypted string: ', end='')
for item in result:
    print(chr(item), end='')
print('\nkey: ', end='')
print(key)

key_index = 0
for i in range(0, len(result)):
    if result[i]>=97 and result[i]<=122:
        result[i] = result[i]-key[key_index]
        key_index += 1
        if result[i]<97:
            result[i] = result[i]+26
print('decrypted string: ', end='')
for item in result:
    print(chr(item), end='')