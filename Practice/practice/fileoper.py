#open file read file
f = open("die4.txt","rb") #text mode b=binary
t = open("mycopy.png", "wb")
#readfile
#print(file.read()) #string
t.write(f.read())
#close
f.close()
t.close()