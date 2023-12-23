#while loop
#i = 1
#while i <= 10:
  #  print(i)
   # i+=1

#print ("while loop ended")

#forloop

for alphabets in "panjagala chinna veera bhadrudu":
    print(alphabets)

#defining array now

friends = ["ragahava", "prashanth", "krishna", "mani", "viswa"]
for name in friends:
    print(name)

#now lets try print numbers by defining range in loop

for numbers in range(10):
    print(numbers)

#now lets try to print numbers by defining range between two numbers

for numbers in range(3, 10):
    print (numbers)

# now lets try to use length array

friends = ["ragahava", "prashanth", "krishna", "mani", "viswa"]
print(len(friends))
for index in range(len(friends)):
    print(friends[index])

# using if conditions within for loop

for numbers in range(10):
    if numbers == 0:
        print("first Iteration")
    elif numbers == 1:
        print ("second iteration")
    else:
        print (numbers)