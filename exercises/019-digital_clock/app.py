#Complete the function to return how many hrs and min are displayed on the 24th digital clock.
def digital_clock(n):
  horas=n/60
  if horas>60:
    horas/60
  return int(horas), int((horas%1)*60)

#Invoke the function with any interger (seconds after midnight)
print(digital_clock(194))
