#Complete the function to return the tens digit of a given interger
def tens_digit(num):
  strnum=str(num)
  return int(strnum[len(strnum)-2])


#Invoke the function with any interger.
print(tens_digit(854345))