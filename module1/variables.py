'''

temperature = 96.8

emri = "milot"

mosha= 12.3

print(type(mosha))
print(type(temperature))
print(type(emri))
'''

#Kalkulime

x = 8

y = 10

result = x+y

print(result)

#update values

age = 30

age+=1

print(age)

#combine values

first_name = "Uvi"
last_name = "Muvi"

full_name = first_name +" "+last_name

print(full_name)

#array (lists)

fav_colors = ["red", "green", "blue", "yellow", "purple"]
first = fav_colors[0]
second = fav_colors[1]

print(first)
print(second)

#methods for list
#append - add an item at the end of the list
fav_colors.append("orange")
print(fav_colors)

#insert - add element in a specific index
fav_colors.insert(2, "white")
print(fav_colors)

#remove

fav_colors.remove("blue")
print(fav_colors)

del fav_colors[4]

print(fav_colors)

#update

fav_colors[0] = "pink"
print(fav_colors)