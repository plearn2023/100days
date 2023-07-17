row1=["A","B","C"]
row2=["D","E","F"]
row3=["G","H","I"]
map=[row1,row2,row3]
print(map)
print(f"{row1}\n{row2}\n{row3}\n")

# print(map[2][2])
position = input("Where do you want to put the treasure? ")
rcolumn=int(position[0])
rrow=int(position[1])
column = rcolumn-1
row = rrow-1
print(map[row][column])
map[row][column]="X"
print(f"{row1}\n{row2}\n{row3}\n")



# print(map)