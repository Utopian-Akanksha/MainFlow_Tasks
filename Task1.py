# Basic Operations related to Lists, Dictionaries and Sets

list1 = ["Apple","Microsoft","Amazon","Nvidia"]

#add
list1.append("Nvidia")

#remove
list1.remove("Amazon")

#update
list1.insert(2,"Facebook")

print(list1)



dict1 = {
    "Name":"Sachin Tendulkar",
    "Age":23,
    "Profession":"Cricketer",
    "Country":"India"
}

#add
dict1["Jersey-no"] = 10

#remove
dict1.pop("Country")

#update
dict1.update({"IPL-team":"Mumbai Indians"})

print(dict1)



set1 = {8,16,24,32,40,48,56}

#add
set1.add(64)

#remove
set1.remove(32)

#update
set1.discard(40)
set1.add(72)

print(set1)
