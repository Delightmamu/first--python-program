#variables = a container for a value
# strings= series of characters
name = "My mom"
compare= "is the best "
nickname = "Mrs loud and clear"
fav_color = "blue"
food = "rice"
hobby = "plants flowers"
weakness = "always put others first"
strengths = "positive ,hard working,patient,perseverance"
her_words = "Nokue,there is nothing that God cant do always depend on him"
in_short= "she is the best thing that ever happened to me"
print(name)
print(compare)
print(f"we call her {nickname}")
print(f"her favourite color is {fav_color}")
print(f"she likes eating {food}")
print(f"during her spare time she {hobby}")
print(f"she is so kind that she {weakness}")
print(f"she is also {strengths}")
print(f"she always tells me {her_words}")
print(f"{in_short} I love her so much.")

#intergers 
money = 20
spend = 15
day = 5
future = 300
days = 1 
print(f"i have {money} dollars")
print(f"i have to spend only {spend} dollars in {day} days")
print(f"but when i become abillionaire i will spend more than{future}dollars in{days} day")


#intergers(int)
#operaters
cars= 10
cars +=5
cars*=2
cars//=5

print(cars)
dress = 50
dress /= 5
print(dress)

#floats
age= 27
km = 4.5
print(f"he is{age} but he walke {km} km everday")



#Boleans
print(7==7)
print(7>7)

is_raining = True
is_sunny = False
if is_raining:
    print("it is raining")
else:
    print("it is sunny")

is_adult = False
is_student = True
if is_adult:
    print("she is an adult")
else:
    print("she is still a baby")

is_open = True
is_closed = False
if is_open:
    print("the shop is still open")
else:
    print("the shop is closed")



#List
girls = ["nokue","nenyasha","anesu","ano"]
boys = ["sean","nigel","tapiwa"]
mixed_list = ["nokue",20,14,"apples"]
colors = ["red","white","blue"]
print(girls)
print(boys)
print(mixed_list)
print(colors)

#list slicing
girls = ["nokue","nenyasha","anesu","ano"]
girls.remove("nokue")
print(girls)
girls.pop(0)
print(girls)

girls.clear
print(girls)
girls.append("ano")
print(girls)
 
 #conditionals

if day == "Monday":
    print("start of the week")
elif day =="Friday":
    print("almost weekend")
else:
    print("just another day")


#nested if statement
if age >= 18:
    if age >= 65:
        print("you are a senior citizen")
    else:
        print("you are an adult")
else:
    print("you are a minor")

    #condition with and

    if age >= 18 and "is_allowed": 
     print("you can watch the movie")


    #type casting

    name = "nokue"
    number = 20
    set = {"boys"}
    print(type(name))
    print(type(set))

boys = 50
print(boys)
print(type(boys))

girls = 70
print(girls)
print(type(girls))

name = "nokue"
print(name)
print(type(name))

km = 20.1
print(km)
print(type(km))

girl = True
print(girl)
print(type(girl))

#user inputs
#name = input("Enter the artist you like:")
#print(f"i also like {name}")


#school =input ("Enter the name of your school:")
#print(f"i also went learned at {school}")

#clothes = input("enter the clothes you like to wear:")
#shoes = input("enter your favourite type of shoes:")
#jewellery = input("enter your jewellery:")
#print(f"great {clothes} suit you well")
#print(f" {shoes} also match with {clothes}")
#print(f"you like expensive{jewellery}")

#braids = input("what type of braids do you want:")
#price = int(input("how much do you have:"))
#print(f"ok you can get {braids} for {price}")

#sets,tupples



A = {1,2,3,4,5,6}
B = {7,8,9,}
print(A&B)

set = {1,2,3,4,5}
set2 ={5,3,4,6,7,8,9}
#set operations
union_set = set |set2
union_set = set2.union(set)
print(union_set)

#intersection
#int_set=set.intersection(set2)
int_set = set & set2
print(int_set)


i = 10
while i < 10:
    print(i)
    i + 1


i = 10
while i > 0:
    print(i)    
    i -= 1    

    h = 100
    while h > 200:
     print(h)
     h -1

     #functions
def greet():
    print("hello guys!!")

greet()


def add(a,b):
    return a +b 

result = add(5,3)
print(result)

def multiply(a,b):
    return a * b

result = multiply(4,2)
print(result)

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
    print(is_even(10))
    print(is_even(7))
     
      