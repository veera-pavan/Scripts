# here we are gonna trying to learn handling 2 dimention values using list

number_grid = [
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [9]
]
#print(number_grid[<row value><column value>]) to access particular value, lets try to access value 8.
print (number_grid[2][2])

#now let try to access all the values using nested for loop

for row in number_grid:
    for col in row:
        print(col)



