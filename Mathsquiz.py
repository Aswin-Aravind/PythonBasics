import random
score=0
for i in range(5):
  num1 = random.randint(0,50)
  num2 = random.randint(0,50)
  n = num1+num2
  print(num1,"+",num2,"=")
  answer = int(input("Enter the answer:"))
  if answer == n:
     score = score+1
     print("Correct")
  else:
     print("Wrong, try again.")
print("You got",score,"/ 5.")