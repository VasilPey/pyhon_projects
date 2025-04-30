print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
#ako slojish .lower nakraq na liniq 26 ne sa nujni proverkite za glavni bukvi nikude
choice1=input("Your on a crossroad which patch do you take left or right?")
if(choice1 == "left" or choice1 == "Left"):
    choice2 =input("you are at a lake u swim or wait:")
    if (choice2 == "wait" or choice2 =="Wait"):
        choice3=input("You waited and when u take the boat there are 3 doors with different color - Blue, Yellow, Red what door do you choose? ")
        if (choice3 == "Yellow" or choice3 == "yellow"):
            print("Congrats u win")
        elif choice3 == "Red" or choice3 == "red":
            print("Wrong door buddy.Game Over")
        elif choice3 == "Blue" or choice3 == "blue":
            print("Wrong door buddy.Game Over")
        else:
            print("THERE ISNT SUCH DOOR BUDDY")
    elif(choice2 == "swim" or choice2 == "Swim"):
        print("No SWIMMING.Game Over")
    else:
        print("yobani v rot")
elif(choice1 == "right" or choice1 == "Right"):
    print("Wrong direction bud.Game Over")
else:print("Wrong fcking INPUT")
