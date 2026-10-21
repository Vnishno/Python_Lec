class User:
    status = "Active"

    def __init__(self, username, email, age):
        self.username = username
        self.email = email
        self.age = age

    def get_info(self):
        print(f"მომხმარებელი: {self.username}")
        print(f"ელ-ფოსტა: {self.email}")
        print(f"ასაკი: {self.age}")
        print(f"სტატუსი: {User.status}")
        print("=" * 40)


user1 = User("nishno", "nishno@gmail.com", 25)
user2 = User("giorgi16", "giorgi16@gmail.com", 22)

user1.get_info()
user2.get_info()

print(f"User 1 - {user1.status}")
print(f"User 2 - {user2.status}")