import time


Data={
    "espresso":{
        "ingrediant":{
            "water":50,
            "milk":25,
            "coffee":18,
        },
        "cost":2,
    },
    "latte":{
        "ingrediant":{
            "water":200,
            "milk":150,
            "coffee":24,
        },
        "cost":2.5,
    },
    "capoccino":{
        "ingrediant":{
            "water":250,
            "milk":100,
            "coffee":24,
        },
        "cost":3,
    }
}

profit=0
resource = {
    "water":1000,
    "milk":700,
    "coffee":800,
}

def check_resource(item):
    ingrediant = Data.get(item).get("ingrediant")
    for resort,article in zip(resource,ingrediant) :
        if(article <= resort):
            print(f"there are sufficient amount of {resort} ")
        elif(resort != article):
            print("there are no sufficient recources left")
            return False


def cost_coffee(coins:float):
    global cost
    global profit
    returned_coin = 0
    
    while not (float(coins) >= int(cost)):
        print(f"not enough coins, you need to insert another {cost - float(coins)}$ :")
        cost -= float(coins)
        profit += float(coins)
        coins=input()
        
        if(float(coins) > int(cost)):
            print("succesfuly payed !")
            returned_coin = float(coins) - cost
            return returned_coin
        

def current_resouce(ingrediant):
    global resource
    print("the current resources are :")
    for i in ingrediant:
        resource[i] -= ingrediant[i]
    print(resource)
    print(f"the profit {profit}")
    print(f"here is your {item} !")
    
on=True

while on :
    item = input("welcome, please select what would you like (espresso,latte,capoccino) :")
    
    if(item=="of"):
        on = False
        print("fin du programme")
        break
        
    while(item not in Data):
        print("give another item :")
        item = input()
    
    print("\n")
        
    print("the current resources : ")
    print(resource)
    print("\n")
    
    print(f"checking if there is enough resources to make {item} ")
    time.sleep(5)
    answer=check_resource(item)
    
    if(answer == False):
        on = False
        break
    cost=Data[item].get('cost')
    print("============================")
    print(f"that would cost you {cost}$")
        
    coins=float(input("please ensert coins to the machine :"))
        
    returned_coin = cost_coffee(coins)
    print(f"here's your change :{returned_coin}$")
        
    print(f"you're command is under request, please wait couple of time")
    time.sleep(5)
    print("\n")
    print("the command is successfuly surved !\n")
        
    ingrediant = Data[item].get("ingrediant")
    print(f"to prepare {item} there must have:{ingrediant}")
    current_resouce(ingrediant)
        
    print("===========================")
    print("\n")
    answer=input("do you want to continue").lower()
    if(answer == "yes"):
        on = True
    else:
        on = False
    
