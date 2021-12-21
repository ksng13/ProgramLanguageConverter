def findValue(string):
    value=''
    find1=False
    find2=False
    for i in range(len(string)):
        if string[i] == '(':
            find1=True
        if string[i] == ')':
            find2=True
        if find1 and find2:
            return value
        if find1==True and string[i] not in ['(',')']:
            value+=string[i]
        i+=1


lines='''for i in range(len('dsd')):
    print(i)
'''

f = open('test.txt','w')
f.writelines(lines)
f.close()

r = open('test.txt','r')

CppText=''
check=r.readline()
while check!='':
    if 'for' in check:
        i=3
        var=findValue(check)
        if 'len' in var:
            var=var[3:]
    if 'print' in check:
        pass

    check=r.readline()

print(var)
r.close()