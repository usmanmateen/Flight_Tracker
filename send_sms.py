number = "+4447469504601"







if number.startswith('+') == True:
  print(number)
elif number.startswith('07') == True:
  list_num = list(number)
  num = ''.join(list_num[1:11])
  number = str("+44"+num)
  print(number)
else:
  list_num = list(number)
  num = ''.join(list_num[2:14])
  number = str("+"+num)
  print(number)

