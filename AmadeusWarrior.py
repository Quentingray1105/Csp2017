# Warrior introduction

def intro():
  print "You are a Warrior. Choose your weapon."
  warrior()
  
def warrior():
  print "Which weapon choice would you like?\n(a) Take a sword\n(b) Take a Morning Star\n(c) Take a Bow and Arrows(type a letter and press return)"
  answer = raw_input()   # Simple way to obtain text input in Canopy 
  print ("\n" * 4)       # Shows 4 line break
  if answer=="a":        # first decision logic, Boolean Statement calling on Choice_sword
    print "You have chosen the sword"
    choice_sword()        #calls on first choice of sword
  elif answer=="b":     # second decision Else if satement showing that if answer is b it prints statement and calls on mourning_star
    print "You have chosen the Morning Star"
    mourning_star()      #Calls on second choice, mourning star
  elif answer=="c":      # third decision else if statement showing that if c is printed it prints this    
    print "You have chosen the Bow and arrows"
    bow_arrows()         #Calls on third choice, bow and arrows
  else:                 #If none of the choices are chosen this else statement makes it print this and game ends
      print "You can't even pick between 3 letters!!!\nYou're dead.(Press run again and attempt again to be the Ultimate Warrior)" 
 
def choice_sword():     #called in line 14 as the first decision. when called it gives another decision
  print "Which sword do you choose?\n(1) Take a fire sword\n(2) Take Lightning Sword (type a letter and press return)"
  answer = raw_input()   # Simple way to put text to the next decision 
  print ("\n" * 4)      #Shows 4 line break
  if answer=="1":        # first choice in Second Decision if statement that prints and calls on fire_sword
    print "You have chosen the Fire Sword"
    fire_sword()         #Calls on first choice, firesword
  elif answer=="2":     #elif statement second choice in second decision
    print "You have chosen the Lightning Sword"  
    lightning_sword()    #variable that is called in later
  else:                 #else statement that prints  this when any other variable is chosen and game ends
      print "No weapon for you.\nYou're dead(Press run again and attempt again to be the Ultimate Warrior)"
      
def lightning_sword():   #called in line 32 in the second decision. when called the game ends because the warrior dies
    print "You chose the Lightning Sword and you have to fight Jack Black who is running at you like beowulf style"     
    print "Jack Black is like a total beast and turns into Kung Fu Panda and hit you with the 'Skadoosh'\nYou're dead(Press run again and attempt again to be the Ultimate Warrior)"   
def mourning_star():     ##called in line 16 in the first decision. when called the game ends because the warrior dies
    print"You fool! You have nowhere near the training it takes to master the art of the Mourning Star.\nYou swung the Mourning Star and struck yourself in the back. You bled out.\nYou're dead.(Press run again and attempt again to be the Ultimate Warrior)"

def bow_arrows():       #called in line 19 in the first decision. when called the game ends because the warrior dies
    print "Who do you think you are? Katniss Everdeen?!?\nYou're dead.(Press run again and attempt again to be the Ultimate Warrior)"

def fire_sword():          ##called in line 32 in the second decision and creates thwe third and final decision
    print "Scibbiddybobbyboo yeah! You just picked the best freaking sword on the market. If you would've chosen the lightning sword you would've been TOTALLY screwed!"
    print "Now you gotta fight Tyler Perry's household-known, fun lovable character Madea. How are you going to fight this beast? \n(1) Go to the Pit of Misery and fight Madea who is wielding an axe and running at you like a madman. \n(2) Stay still and cry \n(3) Put on your big boy pants on and choke the crap outa Madea"
    answer = raw_input()   # Simple way to put text to the decision
    print ("\n" * 4)      #Shows 4 line break
    if answer=="1":       #First choice in third decision if statement and calls pit_misery
        print "You have chosen to go to the Pit of Misery"
        pit_misery()    #Pit of miserry will be called on later to determine fate
    elif answer=="2":     #Second choice in third decision elif statement and calls sit and cry
        print "You have chosen to sit and cry"
        sit_cry()          #Sit and cry will be called on later to determine fate
    elif answer=="3":    #Third choice in third decision if statement and calls pit_misery
        print "You have chosen to put on your big boy pants on and choke the crap outa Madea"
        bigboy_pants()     #big boy pants will be called on later to determine fate
    else:                 #else statement that prints  this when any other variable is chosen and game ends
        print "You chocked and did nothing.\nYou're dead.(Press run again and attempt again to be the Ultimate Warrior)"
             
def pit_misery():      ##called in line 52 in the third decision and prints this and ends the game
    print "The 400 pound beast just ambushed you and suffocated you with her ugly gut flabs \nYou're dead(Press run again and attempt again to be the Ultimate Warrior)"

def sit_cry():          ##called in line 55 in the third decision and prints this and ends the game
    print "You wuss! For being such a queer Madea just mistook you for a donut and ate you \nYou're dead(Press run again and attempt again to be the Ultimate Warrior)"

def bigboy_pants():      ##called in line 55 in the third decision and prints this and ends the game because you won
    print "OHHHH YEAH!! You stabbed Madea with your flaming sword in her gut filled with grease. SHE EXPLODED INTO FLAMES AND DIES!\nYou are the ultimate Warrior."
intro()
