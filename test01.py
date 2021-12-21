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

person = {'name':'John','age':66}
print(person)