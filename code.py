#importing libraries
import random

#tank lists used to store info about tanks
dvalist={
  "name":"D.Va",
  "health":"400 health and 200 armour in mech and 150 health out of mech",
  "difficulty":"medium"}
orisalist={
  "name":"Orisa",
  "health":"200 health and 200 armour",
  "difficulty":"medium"}
reinlist={
  "name":"Reinhardt",
  "health":"300 health and 200 armour",
  "difficulty":"easy"}
hoglist={
  "name":"Roadhog",
  "health":"600 health",
  "difficulty":"easy"}
sigmalist={
  "name":"Sigma",
  "health":"300 health and 100 shield",
  "difficulty":"hard"}
winstonlist={
  "name":"Winston",
  "health":"400 health and 100 armour",
  "difficulty":"medium"}
balllist={
  "name":"Wrecking Ball",
  "health":"500 health and 100 armour",
  "difficulty":"hard"}
zaryalist={
  "name":"Zarya",
  "health":"200 health and 200 shield",
  "difficulty":"hard"}
#main and off tank lists and data
maintanks=["Reinhardt","Winston","Orisa","Wrecking Ball"]
offtanks=["Zarya","D.Va","Roadhog","Sigma"]
dvaH=dvalist["health"]
dvaD=dvalist["difficulty"]
orisaH=orisalist["health"]
orisaD=orisalist["difficulty"]
reinH=reinlist["health"]
reinD=reinlist["difficulty"]
hogH=hoglist["health"]
hogD=hoglist["difficulty"]
sigmaH=sigmalist["health"]
sigmaD=sigmalist["difficulty"]
winstonH=winstonlist["health"]
winstonD=winstonlist["difficulty"]
ballH=balllist["health"]
ballD=balllist["difficulty"]
zaryaH=zaryalist["health"]
zaryaD=zaryalist["difficulty"]


#input loop
flag=True
print("Bot: Hi what type of tanks would you like to know about? (Main Tanks or Off Tanks)")
while(flag==True):
  userinput=input()
  userinput=userinput.lower()
  #tests for using user saying bye and stops code
  if(userinput!="bye"):
    if(userinput=="thanks" or userinput=="thank you"):
      flag=False
      print("Bot: You are welcome..")
      #tests for keywords
    elif(userinput=="main tanks"):
      print("Bot: {} or random".format(maintanks))
      print("Bot: What main tank you would like to learn about?")
      userinput=input()
      userinput=userinput.lower()
      if(userinput=="random"):
        userinput=random.choice(maintanks)
        userinput=userinput.lower()
      if(userinput=="reinhardt"):
        print("Bot: Clad in powered armor and swinging his hammer, Reinhardt leads a rocket-propelled charge across the battleground and defends his squadmates with a massive energy barrier.")
        print("Bot: What would you like to know about Reinhardt? (Health, difficulty)")
        userinput=input()
        userinput=userinput.lower()
        if(userinput=="health"):
          print("Bot: Reinhardt has {}".format(reinH))
        elif(userinput=="difficulty"):
          print("Bot: Reinhardt is {} difficulty to play".format(reinD))
        else:
          print("Bot: I'm sorry, I don't understand")
      elif(userinput=="winston"):
        print("Bot: Winston wields impressive inventions—a jump pack, electricity-blasting Tesla Cannon, portable shield projector and more—with literal gorilla strength.")
        print("Bot: What would you like to know about Winston? (Health, difficulty)")
        userinput=input()
        userinput=userinput.lower()
        if(userinput=="health"):
          print("Bot: Winston has {}".format(winstonH))
        elif(userinput=="difficulty"):
          print("Bot: Winston is {} difficulty to play".format(winstonD))
        else:
          print("Bot: I'm sorry, I don't understand")
      elif(userinput=="orisa"):
        print("Bot: Orisa serves as the central anchor of her team, and defends her teammates from the frontline with a protective barrier. She can attack from long range, fortify her own defenses, launch graviton charges to slow and move enemies, and deploy a Supercharger to boost the damage output of multiple allies at once.")
        print("Bot: What would you like to know about Orisa? (Health, difficulty)")
        userinput=input()
        userinput=userinput.lower()
        if(userinput=="health"):
          print("Bot: Orisa has {}".format(orisaH))
        elif(userinput=="difficulty"):
          print("Bot: Orisa is {} difficulty to play".format(orisaD))
        else:
          print("Bot: I'm sorry, I don't understand")
      elif(userinput=="wrecking ball"):
        print("Bot: Wrecking Ball rolls across the battlefield, using his arsenal of weapons and his mech’s powerful body to crush his enemies.")
        print("Bot: What would you like to know about Wrecking Ball? (Health, difficulty)")
        userinput=input()
        userinput=userinput.lower()
        if(userinput=="health"):
          print("Bot: Wrecking Ball has {}".format(ballH))
        elif(userinput=="difficulty"):
          print("Bot: Wrecking Ball is {} difficulty to play".format(ballD))
        else:
          print("Bot: I'm sorry, I don't understand")
      else:
        print("Bot: I'm sorry, I don't understand")
  
    elif(userinput=="off tanks"):
      print("Bot: {} or random".format(offtanks))
      print("Bot: What off tank you would like to learn about?")
      userinput=input()
      userinput=userinput.lower()
      if(userinput=="random"):
        userinput=random.choice(offtanks)
        userinput=userinput.lower()
      if(userinput=="zarya"):
        print("Bot: Deploying powerful personal barriers that convert incoming damage into energy for her massive Particle Cannon, Zarya is an invaluable asset on the front lines of any battle.")
        print("Bot: What would you like to know about Zarya? (Health, difficulty)")
        userinput=input()
        userinput=userinput.lower()
        if(userinput=="health"):
          print("Bot: Zarya has {}".format(zaryaH))
        elif(userinput=="difficulty"):
          print("Bot: Zarya is {} difficulty to play".format(zaryaD))
        else:
          print("Bot: I'm sorry, I don't understand")
        
      elif(userinput=="d.va"):
        print("Bot: D.Va’s mech is nimble and powerful—its twin Fusion Cannons blast away with autofire at short range, and she can use its Boosters to barrel over enemies and obstacles, or deflect attacks with her projectile-dismantling Defense Matrix.")
        print("Bot: What would you like to know about D.va? (Health, difficulty)")
        userinput=input()
        userinput=userinput.lower()
        if(userinput=="health"):
          print("Bot: D.Va has {}".format(dvaH))
        elif(userinput=="difficulty"):
          print("Bot: D.Va is {} difficulty to play".format(dvaD))
        else:
          print("Bot: I'm sorry, I don't understand")
      elif(userinput=="roadhog"):
        print("Bot: Roadhog uses his signature Chain Hook to pull his enemies close before shredding them with blasts from his Scrap Gun. He’s hardy enough to withstand tremendous damage, and can recover his health with a short breather.")
        print("Bot: What would you like to know about Roadhog? (Health, difficulty)")
        userinput=input()
        userinput=userinput.lower()
        if(userinput=="health"):
          print("Bot: Roadhog has {}".format(dvaH))
        elif(userinput=="difficulty"):
          print("Bot: Roadhog is {} difficulty to play".format(hogD))
        else:
          print("Bot: I'm sorry, I don't understand")
      elif(userinput=="sigma"):
        print("Bot: Sigma is an eccentric astrophysicist and volatile tank who gained the power to control gravity in an orbital experiment gone wrong. Manipulated by Talon and deployed as a living weapon, Sigma’s presence on the battlefield cannot be ignored.")
        print("Bot: What would you like to know about Sigma? (Health, difficulty)")
        userinput=input()
        userinput=userinput.lower()
        if(userinput=="health"):
          print("Bot: Sigma has {}".format(sigmaH))
        elif(userinput=="difficulty"):
          print("Bot: Sigma is {} difficulty to play".format(sigmaD))
        else:
          print("Bot: I'm sorry, I don't understand")
      else:
        print("Bot: I'm sorry, I don't understand")
    else:
      print("Bot: I'm sorry, I don't understand")
    print("Bot: Hi what type of tanks would you like to know about? (Main Tanks or Off Tanks)")
  else:
    flag=False
    print("Bot: Bye")