import random
import string
response = 'n'
flag = True

def msg_gen(size, chars=string.printable):
    return ''.join(random.choice(chars) for _ in range(int(size)))

while flag:
  length = str(input('How long do you want your message to be?\n'))
  if length.isdigit() != True:
    length = input('That is not a valid input. How long do you want your message to be?\n')
  print(msg_gen(length))
  temp = input('Is this what you wanted to send?\n')
  if temp == 'y' or temp == 'Y' or temp == 'yes' or temp == 'Yes' or temp == 'YES':
    response = 'y'
    flag = False
  elif temp == 'n' or temp == 'N' or temp == 'No' or temp == 'no' or temp == 'NO':
            response = 'n'
  else:
    if temp != 'y' and temp != 'n' :
      print('I\'m sorry. I didn\'t understand that. Please try again.\n')

print('Ending now')
