x=int(input())

#While the number is greater 10 we keep going
while x>=10:
  numbers = [int(i) for i in str(x)]

  count = 1
  for i in range(len(numbers)):
    if numbers[i] != 0: 
      count = count * numbers[i]
  x = count

print(x)