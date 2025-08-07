class UserInfo :
    pass

user = UserInfo()

user.name = "satya"
user.id = "1"
print(user.name)
print(user.id)

# UserInfo().name = "helie"
# print(UserInfo().name)

# reduce codes
class User() :
    def __init__(self,username,id):
        self.id = id
        self.username = username
        self.follower = 0
        self.following = 0

    def follow(self,user):
        user.follower += 1
        self.following += 1

user1 = User("satyajit","1")
user2 = User("helie","2")

user1.follow(user2)

print("user 1 :follower" , user1.follower)
print("following" , user1.following)

print("user 2 :follower" , user2.follower)
print("following" , user2.following)