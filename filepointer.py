with open("Text.txt",'r') as f:
    content = f.read()
    print(content)
fi = open('Text.txt','r')
print("The filepointer is at byte:",fi.tell()) # the tell() method helps us to find the position of the file pointer
con = fi.read()
print("after reading the file pointer is at",fi.tell())

#Modifying file pointer
# <file-ptr>.seek(offset[, from)
fi.seek(10)
print(" The file pointer is at",fi.tell())

