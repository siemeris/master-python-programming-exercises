#Complete the function to return the number of day of the week for k'th day of year. 
def day_of_week(k):
  dia=0
  # El día 1 es 4-jueves
  return (3+k)%7

#Invoke function day_of_week with an interger between 0 and 6 (number for days of week)
print(day_of_week(56))