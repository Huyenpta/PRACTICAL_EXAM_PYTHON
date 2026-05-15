class User:
    def __init__(self, name, age):#self như this trong java
        self.name = name
        self.age = age

    def say_hello(self):
        print("Hello, I'm", self.name)
    
U = User("Nguyen Van A", 20)
U.say_hello()

class VipUser(User):#VipUser kế thừa từ User
    def __init__(self, name, age, balance):
        super().__init__(name, age)
        self.balance = balance
    def show_money(self):
        print("Balance:",self.balance)

v=VipUser("Nguyen Van B", 25,1000)
v.say_hello()
v.show_money()

class Guest: #Guest không kế thừa từ User, nhưng vẫn có phương thức say_hello
    def say_hello(self):
        print("Goodnight.")
g = [User("Nguyen Van A",20), Guest()]
for u in g:
    u.say_hello()




