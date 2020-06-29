def average(nums, size):
 return sumNums(nums,size)/size

def sumNums(nums, size):
 total = 0
 for index in range(size):
   total = total + nums[index]
 return total

def main():
 numbers = []
 keepGoing = "y"
 print("This program calculates averages")
 new_number= int(input(" Please enter a number here: "))
 while keepGoing == "y":
  print("Do you want to enter another number?")
  keepGoing = input("(Enter y for yes.)").lower()
  if keepGoing == "y": 
    new_number= int(input(" Please enter a number here: "))
    numbers.append(new_number)
  else:
    print("Thanks") 
 size = len(numbers)

 print("The average of the numbers that you entered is", average(numbers,size))

main()