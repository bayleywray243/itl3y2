import pandas as pd #importing pandas lib so that the code functions properly 

df1 = pd.read_json("train.json") 

data = df1.to_dict()


liked_ingredients = [] 
disliked_ingredients = [] 

def like():
  inglike = input("Enter an ingredient you would like in your recipe: ")
  liked_ingredients.append(inglike)

def dislike():

  ingdis_like = input("Enter what you don't like: ") #asks what the user likes
  disliked_ingredients.append(ingdis_like)

like_counter = 0

while like_counter < 5: #alots the user 5 liked ingredients
  like()#
  like_counter += 1

  dislike_counter = 0

while dislike_counter < 2: #alots the user 2 disliked ingredients
  dislike()#
  dislike_counter += 1

for x in data['id']:

  for t in liked_ingredients:
    if t in data['ingredients'][x] and t not in disliked_ingredients:
#print remove cuisine that has disliked ingredients inside of it

     print("cuisine: ", data['cuisine'][x], "the id is: ", data['id'][x], "The ingredient is: ", t)
# print cuisine that contains liked ingredients only

print("The things you do like: ",liked_ingredients)
print("The things you don't like: ", disliked_ingredients)
