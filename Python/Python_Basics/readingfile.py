#lets now try to read file

filecontent = open('test.txt', "r")

#reading all the lines in .txt file using for loop
for content in filecontent.readlines():
    print(content)

#reading file all the lines with out for loop
print(filecontent.read())

#reading file line by line 

print(filecontent.readline())

#reading file from list

print(filecontent.readlines()[1])

#close the opened file

filecontent.close()


