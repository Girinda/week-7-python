#loops comtrol statements

fruits =["apples", "bananas", "cherry","dates"]

for fruits in fruits
    if fruit == "cherry":
       break # exit the loop is cherry is found
    print(fruit)

or

for fruits in fruits
    if fruit == "cherry":
       continue # skip cherr and move to date
    print(fruit)

or

for fruits in fruits
    if fruit == "cherry":
       pass # placeholder, no action is needed for cherry
    print(fruit)




one example of while loops


count = 0

while count < 5:
      print (count)
      count + = 1
      if count == 3:
      break # exits the loop when the count is reached = 3
