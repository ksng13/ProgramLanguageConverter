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

def findFunctionName(string):
    pass


lines='''for i in range(len('dsd')):
    print(i)
'''

f = open('SimpleInput.txt','w')
f.writelines(lines)
f.close()

r = open('SimpleInput.txt','r')

CppText=''
check=r.readline()
while check!='':
    if 'for' in check:
        i=3
        IntValue=findValue(check)
        while 'len' in IntValue:
            IntValue=IntValue[3:]
        IntValue=int(IntValue)
    if 'print' in check:
        StringValue=findValue(check)
    if 'def' in check:
        FunctionName=findFunctionName(check)
    check=r.readline()

print(IntValue)
r.close()