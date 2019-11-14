'''def reverseS(mystr):
    #base case
    if mystr=="":
        return ""
    #general case ---> smaller version
    else:
        first = mystr[0]
        return  reverseS(mystr[1:]) + first

print(reverseS("greatjob"))'''

'''def reverseS(mystr):
    #base case
    if len(mystr)==1:
        return mystr
    #general case ---> smaller version
    else:
        last = mystr

print(reverseS("greatjob"))'''

def reversewl(wordlist):
    #base case
    if len(wordlist) <=3:
        return wordlist
    #general case
    else:
        first = wordlist[0]
        return reversewl(wordlist[1:]) + first

#test function
strgs = "cat is running"
wlist = strgs.split(" ")
print(reversewl(wlist))