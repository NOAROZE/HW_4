# START
pizza: int = int(input("enter a num of pizza:"))
pizza_of_friends = pizza // 4
print(f"number of pizza of friends: {pizza_of_friends}")
rest = pizza % 4
print(f"number of rest of friends: {rest}")
# END

# START
pizza1: int = int(input("enter a num of pizza:"))
friends: int = int(input("enter anum of friends:"))
pizza_of_friends = pizza1 // friends
print(f"number of pizza of friends: {pizza_of_friends}")
rest = pizza1 % friends
print(f"number of rest of friends: {rest}")
# END