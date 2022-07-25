#Complete the function to calculate how many hours and minutes are passed since midnight.
def hours_minutes(secs):
  horas=0
  if secs > 3600:
    horas=int(secs/3600)
    minutos=round(((secs/3600)%1)*60)
  
  elif secs >=60:
    minutos=int(secs/60)

  return horas,minutos

#Invoke the funtion and pass any interger as its argument.
print(hours_minutes(360))