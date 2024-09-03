coffees = {
    "Espresso" : [50, 0, 18, 1.5],
    "Latte" : [200, 150, 24, 2.5],
    "Cappucino" : [250, 100, 24, 3]
}
machine = [300, 200, 100, [0, 0, 0, 0]] # Water, Milk, Coffee, [1c, 5c, 10c, 25c]

def report():
    print("Water: ", machine[0])
    print("Milk: ", machine[1])
    print("Coffee: ", machine[2])
    print("Money", (machine[-1][0] + machine[-1][1] * 5 + machine[-1][2] * 10 + machine[-1][0] * 25))


def check_resource_sufficiency(coffee_type):
    to_return = 1
    if coffee_type == "Espresso":
        if machine[0] < 50 :
            print("Sorry there is not enough water\n")
            to_return = 0
        if machine[2] < 18:
            print("Sorry there is not enough coffee\n")
            to_return = 0
    elif coffee_type == "Latte": 
        if machine[0] < 200:
            print("Sorry there is not enough water\n")
            to_return = 0
        if machine[1] < 150:
            print("Sorry there is not enough milk\n")
            to_return = 0
        if machine[2] < 24:
            print("Sorry there is not enough coffee\n")
            to_return = 0
    elif coffee_type == "Cappucino":
        if machine[0] < 250:
            print("Sorry there is not enough water\n")
            to_return = 0
        if machine[1] < 100:
            print("Sorry there is not enough milk\n")
            to_return = 0
        if machine[2] < 24:
            print("Sorry there is not enough coffee")
            to_return = 0
    return to_return

def process_coins(answer): # I misunderstood this part and fucked myself. Its been late and I will deal with this later.
    print("Coffee of your choice costs: ", coffees[answer][-1])
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    total_money_entered = quarters*0.25 + dimes*0.10 + nickels*0.05 + pennies*0.01
    if total_money_entered < coffees[answer][-1]:
        print("Sorry that's not enough money. Money refunded")
    else:
        owed = coffees[answer][-1]
        required_quarters =  owed / 0.25
        if required_quarters < quarters:
            machine[-1][-1] += quarters
            owed = total_money_entered - quarters * 0.25
            required_dimes = owed / 0.1
            if required_dimes < dimes:
                machine[-1][-2] += dimes
                owed = total_money_entered - dimes * 0.1
                required_dimes = owed / 0.05
            else:
                machine[-1][-2] += required_dimes
                to_return = (dimes -required_dimes)*0.10 + nickels*0.05 + pennies*0.01
                print("You have been refunded: ", to_return)
        else:
            print("Enough quarters")
            machine[-1][-1] += required_quarters
            to_return = (quarters - required_quarters)*0.25 + dimes*0.10 + nickels*0.05 + pennies*0.01
            print("You have been refunded: ", to_return)
            
    

def menu():
    answer = 1
    while answer != "exit":
        answer = input("What would you like? (Espresso/Latte/Cappucino)")
        if answer == "Espresso" or answer == "Latte" or answer == "Cappucino":
            situation = check_resource_sufficiency(answer)
            if situation == 1:
                process_coins(answer)
        elif answer == "report":
            report()

if __name__ == "__main__":
    menu()