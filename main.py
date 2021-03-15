###Solution to problem 65 from ben stephenson's "the python workbook".

def get_more_values():
  print('Enter the coordinates (blank to quit):')
  return input()

results = []
perimeter = 0

print('Enter the coordinates:')
mystr_ = input()
results.append(mystr_.split(','))

while mystr_ != '':
  mystr_ = get_more_values()
  if mystr_ != '':
    results.append(mystr_.split(','))
    if len(results) >= 2:
      last_value = results[-1]
      last_value = [float(i) for i in last_value]
      second_to_last_value = results[-2]
      second_to_last_value = [float(i) for i in second_to_last_value]

      perimeter = perimeter + ((last_value[0] - second_to_last_value[0]) ** 2 + (last_value[1] -  second_to_last_value[1]) ** 2) ** 0.5
  elif len(results) >= 2:
      last_value = results[-1]
      last_value = [float(i) for i in last_value]
      first_value = results[0]
      first_value = [float(i) for i in second_to_last_value]
      if not (first_value == last_value):
        perimeter = perimeter + ((last_value[0] - first_value[0]) ** 2 + (last_value[1] -  first_value[1]) ** 2) ** 0.5 
print(perimeter)
