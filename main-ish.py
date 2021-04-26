print("Hey there. I haven't used Python before, so bare with me.\n I declare the current year as a variable and then mod it to see if it's a leap year or not. the variable leapyear will keep track of it")



leapyear = "false";
currentyear = 2021;

if currentyear%400 == 0:
     leapyear = "true";

elif currentyear%100 == 0:
     leapyear = "false"

elif currentyear%4 == 0:
     leapyear = "true";


print("the statement: this year is currently a leap year holds...");
print(leapyear);