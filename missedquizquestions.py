for number in range(1, 9)
  if number % 10 == 0:
    break
else:
    print("Let's print something out")

#the break statement above never prints because 1,2,3,4,5,6,7,8 % 10 are not equal to 0, so the if block is never executed and the else block is executed

#will the print statement be reached in this code?
for number in range(1, 100):
  if number % 10 == 0:
    break
else:
  print("Let's print something out!")

#print statement will not be executed because 10 % 10 == 0, so the inner if block will execute, breaking the loop, and because nothing after break executes, nothing is printed 

#what is the output?

movies = ['vikings', 'soldiers', 'ss', 83, 11, -8.7e^2]
for m in range(-3):
  print(movies[m])

#output: nothing because you can't print negative indicies 

#what is the value of int('101', 2)
#5 - since 10 ^ 2 + 1 = 101, you can take the number on the right hand side of the comma and subsitute the old base (10) with this number to get 2 ^ 2 + 1 = 5

#what class might be used to store precise monetary amounts for a banking application?
#anwser - double not float because floats are prone to floating point errors

#what is the value of this statement? bool(-1) == 1
#anwser: true

#what does bytes 4 do?
#anwser: it creates an empty bytes object 4 bytes long - aka each byte has 2 bits with 0 or 1, so 2 times 4 = 8 meaning computers are made of 8 bits

