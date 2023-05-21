 #database input and making list of elements
data1 = open("data.txt","r")
data2 = data1.split(",")
names = []
prices = []
movements = [] 
idx = 1
idy = 1

for i in data2:
  names.append(i.split(":")[0])
for i in data2:
  idx = i.find(":")
  idy = i.find(";")
  movements.append(i[idx+1:idy])
for i in data2:
  prices.append(i.split(";")[1])

#movement input and check
interestedMovement = input("Please enter the movement name that you want to purchase: ")
idM = -2
try:
  idM = movements.index(interestedMovement)
except ValueError:
  print("There are no paintings belonging to " + interestedMovement + ".")
finally:
  pass

#budget input
wantedPrices = 0
if idM != -2:
  budget = input("Please enter the amount of money you have (in million): ")
  idB = prices[idM].find("M")
  price = float(prices[idM][0:idB])

  #book input and check contemporarily budgets, movement compatibility,and book storage 
  interestedBook = input("Please enter the name of the painting that you want to buy: ")
  interestedBookList = interestedBook.split(",") 
  for i in interestedBookList:
    if i not in names:
      wantedPrices = -1
      print(i, "is not in the database.")
    elif movements[names.index(i)] != interestedMovement:
      wantedPrices = -2
      print(i, "does not belong to", interestedMovement ,"movement.")
    else:
      price = float(prices[names.index(i)][0:-1])
      wantedPrices += price      
  if wantedPrices <= float(budget) and wantedPrices != -1 and wantedPrices != -2:
    print("You have successfully purchased " + interestedBook + ".")
  elif wantedPrices > float(budget):
    print("Willing painting(s) value(s) are higher than your current budget.")
