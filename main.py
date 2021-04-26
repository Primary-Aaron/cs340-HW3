print("Hey there. I haven't used Python before, so bare with me.\n I declare the current year as a variable and then mod it to see if it's a leap year or not. the variable leapyear will keep track of it")

loop = True
leapyear = "false";
while loop:
  try:
      userInput = input("what year?  ")
      loop = False
      val = int(userInput)
  except ValueError:
      print("That's not an int!")
      loop = True
currentyear = int(userInput);

if currentyear%400 == 0:
     leapyear = "true";

elif currentyear%100 == 0:
     leapyear = "false"

elif currentyear%4 == 0:
     leapyear = "true";


print("the statement: That year is/was/will be a leap year holds...");
print(leapyear);