class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        print(f"New user being created: {self.username}\nFollowers: {self.followers}\nFollowing: {self.following}")


    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("0010", "Boma")
user_2 = User("0020", "James")
print("After following: ")
user_1.follow(user_2)

print(f"User 1: {user_1.username}\nFollowers: {user_1.followers}\nFollowing: {user_1.following}")
print(f"User 2: {user_2.username}\nFollowers: {user_2.followers}\nFollowing: {user_2.following}")
# user_1.id = "001"
# user_1.username = "Boma"
# user_2 = User()
# user_2.id = "002"
# user_2.username = "Angela"
# print(user_2.username)
