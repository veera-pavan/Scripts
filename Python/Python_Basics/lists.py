lucky_numbers = [1,2874,23,145,23456]
#prints number in ascending order
lucky_numbers.sort()
lucky_numbers.reverse()
print(lucky_numbers)
friends = ["mani", "khadir", "prashanth", "raghava", "krishna"]
print(friends)
friends[-1] = "conwoy"
print(friends[2])
print(friends[-3])
print(friends[3])
print(friends[3:])
print(friends[1:4])
print(friends[-1])

#list functions
friends.extend(lucky_numbers)
friends2 = ["john", "abraham", "mahatma", "sardar", "subhash"]
#appends new name
friends2.append("manmohansingh")
#inserts new name on index number basis
friends2.insert(1, "rahul")
friends2.remove("abraham")
#removes all the values in the list
#friends2.clear()
print(friends2)
#removes last name in 
friends2.pop()
friends3 = ["anand", "ravi", "eagarly", "bakwas", "kayre"]
#prints name index number
print(friends3.index("anand"))
#prints name count in the list
print(friends3.count("ravi"))
#prints name in alphabatic order
friends3.sort()
print(friends3)

#tuples are same like list which stores values, but they are not editable it uses paranthesis "()" to store values unlike list"[]"
my_numbers = (1,2,3,234)
print (my_numbers.index(1))
my_numbers.insert(1, 248)
print(my_numbers)


