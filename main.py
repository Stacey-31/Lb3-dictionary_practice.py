####Step2
dict_grocery = {"chicken":1.59,
"Beef":1.99,
"Cheese":1.00,
"Milk":2.50}
#print(dict_grocery)
chicken_price = dict_grocery ["chicken"]
#print(chicken_price)
Beef_price = dict_grocery["Beef"]
#print(Beef_price)
Cheese_price = dict_grocery["Cheese"]
#print(Cheese_price)
Milk_price = dict_grocery["Milk"]
#print(Milk_price)

###Step 3
Clothes = {"Shirts":1,
"Sweaters":2,
"Dresses":3,
"Shorts":4}

###Step3
favorite_clothes = Clothes ["Shirts"]
#print(favorite_clothes)

#StepIV
Clothes["Shirts"] = 78 #how we change something in our dictionary
#print(Clothes)

Clothes["jewelry"] = "5" #how we add something to our dictionary
#print(Clothes)

del Clothes["Sweaters"] #how to delete something to our dictionary
#print(Clothes)

#STEP1
list_of_cities = ("Oakland","Atlanta","New York City","Seatle", "Memphis", "Miami", "Boston", "Los Angeles", "Denver" )
#print(list_of_cities)
list_of_cities[2]
favorite_cities = list_of_cities[5:8]
print(favorite_cities)

list_of_kdrama = ("Boys over flowers", "Vicenzo", "IOTNBO", "Sky Castle", "Reply_1997", "Mr Queen", "WWWSK","Reply_1988", "A Korean Odyssey","TWWB")
#print(list_of_kdrama)
Mustwatch_kdrama = list_of_kdrama[1:6]
print(Mustwatch_kdrama)

#StepV
list_of_cities[0] = "San_Francisco"
list_of_cities[2] = "Brooklyn"
list_of_cities[7] = "Hollywood"
list_of_cities[5] = "Tampa"
print(list_of_cities)