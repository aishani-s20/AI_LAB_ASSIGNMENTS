class Restaurant:
    def __init__(self, name, cuisine):
        self.restaurant_name=name
        self.cuisine_type=cuisine
    
    def describe_restaurant(self):
        print("Restaurant name is:",self.restaurant_name)
        print("Cuisine type is:",self.cuisine_type)
    
    def open_restaurant(self):
        print("Restaurant is open")

r1=Restaurant("China Town", "Chinese")
print("name:",r1.restaurant_name)
print("cuisine:",r1.cuisine_type)

r1.describe_restaurant()
r1.open_restaurant()

class User:
    def __init__(self,fname,lname,age,gender,city):
        self.first_name=fname
        self.last_name=lname
        self.age=age
        self.gender=gender
        self.city=city

    def describe_user(self):
        print("first name:",self.first_name)
        print("last name:",self.last_name)
        print("age:",self.age)
        print("gender:",self.gender)
        print("city of residence:",self.city)
    
    def greet_user(self):
        print("Hello",self.first_name,self.last_name)

user1=User("Aliya", "Shetty",20,"F","Mumbai")
user2=User("Daksh","Chauhan",19,"M","Delhi")

user1.greet_user()
user1.describe_user()

user2.greet_user()
user2.describe_user()

