haveIng=list()
fridge=dict()

fridge.update({"rice":50})
fridge.update({"yogurt":10})
fridge.update({"juice":20})
fridge.update({"oil":50})
fridge.update({"bananas":15})
fridge.update({"berries":20})
fridge.update({"eggs":10,"mushrooms":20,"peppers":3,"cheese":2,"tomatos":4,"milk":3})
fridge.update({"water":100,"bread":20,"carrots":3,"sausage":2,"pasta":4,"lime":3})


omlet_ingredients={"eggs":2, "mushrooms":5, "peppers":1, "cheese":1, "milk":1}
fries_ingredients={"mushrooms":3,"peppers":2,"tomatos":2,"rice":10}
eggcheese_ingredients={"eggs":100,"cheese":2}
loveBanana_ingredients={"bananas":10,"yogurt":5,"musli":10}





print(fridge)
n=1

while n==1:

    food = dict()
    print("1-omlet \n 2-fries \n 3-eggcheese \n 4-loveBanana \n")
    cook=int(input("please enter which cook do you want:(to finish enter 0)"))
    k = 0


    if cook==1:
        food = omlet_ingredients
    elif cook==2:
       food =fries_ingredients
    elif cook==3:
        food=eggcheese_ingredients
    elif cook==4 :
       food=loveBanana_ingredients
    else:
        print("see you... ")
        break


    for ingredients, numbers in food.items():
        if fridge.get(ingredients) != None:
            print("there is " + ingredients)

            if fridge.get(ingredients) >= numbers:
                print("it has enough " + ingredients)
                haveIng.append(True)
                haveIng.append(ingredients)
            else:
                print("not enough " + ingredients + " to do that food")
                haveIng.append(False)
                haveIng.append(ingredients)
                k = k - 1
        else:
            print("we have no " + ingredients + " in fridge")
            haveIng.append(False)
            haveIng.append(ingredients)
            k = k - 1


    print("-"*20)
    if k==0:
        print("this cook can be done")
    elif k==1:
        print("see you")
    else:
        print("this cook can not be cook")


    try:
        fridge("rice")>100
    except(KeyError,TypeError) as error:
        print(" there is a problem")


