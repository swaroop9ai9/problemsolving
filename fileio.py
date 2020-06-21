fileptr=open("text.txt",'w')
if fileptr:
    print("file is opened successfully")
content = fileptr.readline();
print(content)
fileptr.close()


#file = open("Text.txt","r+")
#i = input("Append any text?")
#file.write(i)
#file.close()

#file = open("Text.txt","r");
#content = file.readline();
##print("Type of content is: "+ str(type(content)))
#print(content)
#file.close()

print("File created succesfully")
