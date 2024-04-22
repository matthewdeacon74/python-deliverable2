# store user name
userName = input("Hello customer, what is your name? ")

#fruit options and costs
numapple = 0
appleCost = 2
numGrape = 0
grapeCost = 1
numOrange = 0
orangeCost = 3

subTotal = 0

isDone = False
while isDone == False:
    # display the list of fruits for sale
    print(f"Apples: ${appleCost} each. You have {numapple} in your bag.")
    print(f"Grapes: ${grapeCost} each. You have {numGrape} in your bag.")
    print(f"Oranges: ${orangeCost} each. You have {numOrange} in your bag.")
    print(f"Your current subtotal is ${subTotal}.")
    print("")
    nextBuy = input("What would you like to buy (apple, grapes, orange, or done)?")
    if nextBuy == "apple":
        numapple +=1
        subTotal += appleCost
    elif nextBuy == "grape":
        numGrape +=1
        subTotal += grapeCost
    elif nextBuy == "orange":
        numOrange += 1
        subTotal += orangeCost
    elif nextBuy == "done":
        isDone = True
        print(f"Receipt for {userName}:")
        print(f"{userName} bought {numapple} apples, {numGrape} grapes, and {numOrange} oranges.")
        print((f"{userName}'s subtotal is ${subTotal}."))
        print(f"5% Tax = ${subTotal * .05}")
        print(f"Total Bill: ${subTotal * 1.05}")
    else:
        print("We don't sell that.")

