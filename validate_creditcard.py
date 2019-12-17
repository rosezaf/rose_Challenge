import re
t=input()
def check(string):
    for i in range(0,len(string)-3):
        if string[i]==string[i+1]==string[i+2]==string[i+3]:
            return False
    return True
        
for i in range(0,t):
    string=raw_input()
    if check(string.replace("-",""))==False:
        print"Invalid"
    elif bool(re.match(r"^[4-6][0-9]{3}(-)?[0-9]{4}(-)?[0-9]{4}(-)?[0-9]{4}$",string)):
        print "Valid"
    else:
        print"Invalid"