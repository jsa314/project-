flag=True
while flag == True:
  flag=False
  print("Hello")
  userInput=input()
  userInput=userInput.lower()
  if userInput=="hi":
    print("Hi")
  elif userInput=="hey":
    print("Hey")
  else:
    print("Sorry, I don't understand")
    flag=True