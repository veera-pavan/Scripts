#appending new contenet to the file 
filecontent = open('test.txt', "a")
filecontent.write("\n to fetch some water")

#overwriting content in existing file 

filecontent = open('test.txt', "w")
filecontent.write("\n to fetch some water")

#writing contenet to new file 

#example1:
filecontent = open('test1.txt', "w")
filecontent.write("\n to fetch some water")
#example2:

filecontent = open('test.html', "w")
filecontent.write("<P> This is HTMl </P>")

