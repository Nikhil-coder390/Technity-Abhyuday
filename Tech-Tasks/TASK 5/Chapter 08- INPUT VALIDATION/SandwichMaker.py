#Sandwich Maker
import pyinputplus as pyip
price= {'Wheat': 15, 'White': 10, 'Sourdough': 12, 'Chicken': 25, 'Turkey': 30, 'Ham': 20, 'Tofu': 30, 'Cheddar': 10, 'Swiss': 12, 'Mozzarella': 15, 'Mayo': 3, 'Mustard': 5, 'Lettuce': 7, 'Tomato': 7}

while True:
    order=[]
    bread= pyip.inputMenu(['Wheat', 'White', 'Sourdough'], prompt="Choose bread type- \n", numbered=True)
    order.append(bread)
    protein= pyip.inputMenu(['Chicken', 'Turkey', 'Ham', 'Tofu'], prompt="Choose protein type- \n", numbered=True)
    order.append(protein)
    cheese= pyip.inputYesNo(prompt="Do you want cheese? \n")
    if cheese=='Yes' or cheese=='yes':
        typeof= pyip.inputMenu(['Cheddar', 'Swiss', 'Mozzarella'], prompt="Choose type of cheese- \n", numbered=True)
        order.append(typeof)
    mayo= pyip.inputYesNo(prompt="Do you want mayo? \n")
    if mayo=='Yes' or mayo=='yes':
        order.append('Mayo')
    mustard= pyip.inputYesNo(prompt="Do you want mustard? \n")
    if mustard=='Yes' or mustard=='yes':
        order.append('Mustard')

    lettuce= pyip.inputYesNo(prompt="Do you want lettuce? \n")
    if lettuce=='Yes' or lettuce=='yes':
        order.append('Lettuce')
    tomato= pyip.inputYesNo(prompt="Do you want tomato? \n")
    if tomato=='Yes' or tomato=='yes':
        order.append('Tomato')
    num= pyip.inputInt(prompt="How many sandwiches do you want? ", min=1)
    bill=0
    for ingredients in order:
        cost= price[ingredients]
        bill+=cost
    print("Total bill= ", bill*num)
    ask= pyip.inputYesNo(prompt="Do you want to order something else?")
    if ask=='Yes' or ask=='yes':
        continue
    else:
        break
