from tkinter import *
root=Tk()

def getmenu():
    import random
    from random import choice
    #The two list choices from which a combination of a meal will be produced.
    foods=["rice","ugali","spaghetti","fries","mukimo","chapo","githeri"]
    stews=["beans","njahi","eggs","ndengu","minji","beef","pork","mbuzi","veggies","waru","smokies","no stew"]

    #creating specific stews that will go with a specific main dish
    ricestews=stews[:8]
    ugalistews=stews[5:9]
    spaghettistews=[stews[0],stews[5],stews[6],stews[7],stews[10]]
    friesstews=stews[5:12]
    mukimostews=stews[5:8]
    chapostews=[stews[0],stews[1],stews[3],stews[4],stews[5]]
    githeristews=stews[9:11:2]

    #getting a specific main from the list of foods
    main=random.choice(foods)
    invite=Label(root,text="Your meal for today will be:")
    invite.pack()

    #getting the full meal by from the main dish and a random stew choice to go with it
    if main=="rice":
        meal=str("rice and " + random.choice(ricestews))
    elif main=="ugali":
        meal=str("ugali and " + random.choice(ugalistews))
    elif main=="spaghetti":
        meal=str("spaghetti and " + random.choice(spaghettistews))
    elif main=="fries":
        meal=str("fries and " + random.choice(friesstews))
    elif main=="mukimo":
        meal=str("mukimo and " + random.choice(mukimostews))
    elif main=="chapo":
        meal=str("chapo and " + random.choice(chapostews))
    elif main=="githeri":
        meal=str("githeri and " + random.choice(githeristews))
    else:
        print("You fast today")
    mealIs=Label(root,text=meal)
    mealIs.pack()
#development notes
#instead of using print implement label and work with that
#find an impelement to avoid repetetion of label usage
    
mybutton=Button(root,text="Wanna know what to eat!",command=getmenu,fg="black",bg="red")
mybutton.pack()
root.mainloop()
